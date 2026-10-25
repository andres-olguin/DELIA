import requests
from requests.adapters import BaseAdapter

from backend.network_utils.replay_session import LoggedSession

class Capture(BaseAdapter):
    def __init__(self):
        super().__init__()
        self.sent = None

    def send(self, request, **kwargs):
        self.sent = request
        resp = requests.Response()
        resp.status_code = 200
        return resp

    def close(self):
        pass

def session():
    s, adapter = LoggedSession(), Capture()
    s.mount("https://", adapter)
    return s, adapter

def test_masks_json_body_and_fixes_content_length():
    s, adapter = session()
    s.post("https://x.test", json={"m": "RUT 12.345.678-5 y a@b.co"})
    body = adapter.sent.body
    assert b"12.345.678-5" not in body and b"a@b.co" not in body
    assert b"[[RUT]]" in body and b"[[EMAIL]]" in body
    assert int(adapter.sent.headers["Content-Length"]) == len(body)

def test_masks_str_body():
    s, adapter = session()
    s.post("https://x.test", data="tarjeta 4111 1111 1111 1111")
    assert adapter.sent.body == "tarjeta [[TARJETA]]"

def test_leaves_binary_and_empty_bodies():
    s, adapter = session()
    s.post("https://x.test", data=b"\xff\xfe\x00")
    assert adapter.sent.body == b"\xff\xfe\x00"
    s.get("https://x.test")
    assert adapter.sent.body is None

def test_prints_method_and_url(capsys):
    s, _ = session()
    s.get("https://x.test/p")
    assert "Making GET request to: https://x.test/p" in capsys.readouterr().out

def test_keeps_non_latin1_characters_as_utf8():
    s, adapter = session()
    s.post("https://x.test", data="→ Ñandú a@b.co".encode())
    assert adapter.sent.body == "→ Ñandú [[EMAIL]]".encode()
