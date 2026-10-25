import logging
from io import StringIO

from backend.logger import get_logger

def test_logs_to_given_output():
    out = StringIO()
    get_logger("t-out", output=out).info("hola")
    line = out.getvalue()
    assert "t-out" in line and "INFO" in line and "hola" in line

def test_no_duplicate_handlers():
    get_logger("t-dup", output=StringIO())
    get_logger("t-dup", output=StringIO())
    assert len(logging.getLogger("t-dup").handlers) == 1

def test_level_filters():
    out = StringIO()
    get_logger("t-lvl", level=logging.WARNING, output=out).info("no")
    assert out.getvalue() == ""
