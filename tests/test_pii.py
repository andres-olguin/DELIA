from backend.dlp.pii import detect, redact, rut_dv, nit_dv, luhn

def kinds(text):
    return [f.type for f in detect(text)]

def test_dv():
    assert rut_dv("12345678") == "5"
    assert nit_dv("800197268") == "4"  # NIT de la DIAN
    assert luhn("4111111111111111") and not luhn("4111111111111112")

def test_rut():
    assert kinds("Mi RUT es 12.345.678-5.") == ["RUT"]
    assert kinds("RUT 12345678-5") == ["RUT"]
    assert kinds("RUT 12.345.678-9") == []  # DV incorrecto

def test_nit():
    assert kinds("NIT 800.197.268-4") == ["NIT"]
    assert kinds("NIT 800197268-4") == ["NIT"]
    assert kinds("NIT 800197268-5") == []

def test_cedula_requires_context():
    assert kinds("C.C. 1.234.567.890") == ["CEDULA"]
    assert kinds("cédula 52123456") == ["CEDULA"]
    assert kinds("pedido 52123456") == []

def test_other():
    assert kinds("a.b+c@empresa.co") == ["EMAIL"]
    assert kinds("llama al +57 300 123 4567") == ["TELEFONO"]
    assert kinds("+56 9 8765 4321") == ["TELEFONO"]
    assert kinds("tarjeta 4111 1111 1111 1111") == ["TARJETA"]

def test_redact():
    text, found = redact("Juan (cédula 52123456, juan@x.co)")
    assert text == "Juan (cédula [[CEDULA]], [[EMAIL]])" and len(found) == 2
