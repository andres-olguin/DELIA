from requests import Session

from backend.dlp.pii import redact

class LoggedSession(Session):
    def __init__(self):
        super().__init__()

    # Overriding 'send' catches all methods (.get, .post, .put, etc.) 
    def send(self, request, **kwargs):
        # .path_url gives you just the path (e.g., /api/data), .url gives the full string

        # shortcut: solo enmascara el cuerpo de texto; la URL y los headers no se revisan.
        body = request.body
        was_bytes = isinstance(body, bytes)
        if was_bytes:
            try:
                body = body.decode("utf-8")
            except UnicodeDecodeError:
                body = None  # binario: no se toca
        if isinstance(body, str):
            masked, _ = redact(body)
            request.body = masked.encode("utf-8") if was_bytes else masked
            request.prepare_content_length(request.body)

        print(f"Making {request.method} request to: {request.url}")
        # Call the parent class to actually execute the request
        return super().send(request, **kwargs)

if __name__ == '__main__':
    sess = LoggedSession()
    payload = {
        "project": "Proyecto-TALIA",
        "status" : "testing"
    }

    # httpbin.org is a free service that echoes your request back to you
    response = sess.post("https://httpbin.org/post", json=payload)

    print("Status Code:", response.status_code)
    print("Echoed Body:", response.json().get("json"))