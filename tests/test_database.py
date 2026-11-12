"""Regression tests for database setup and session cleanup."""

import runpy
from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app import database


def test_database_without_url_is_unavailable(monkeypatch):
    monkeypatch.delenv("DANREXO_DATABASE_URL", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)

    config = runpy.run_path(database.__file__)

    assert config["engine"] is None
    with pytest.raises(HTTPException) as exc:
        next(config["get_db"]())
    assert exc.value.status_code == 503


def test_database_import_does_not_connect(monkeypatch, tmp_path):
    db_path = tmp_path / "startup.sqlite"
    monkeypatch.setenv("DANREXO_DATABASE_URL", f"sqlite:///{db_path}")

    config = runpy.run_path(database.__file__)

    try:
        assert config["engine"].url.database == str(db_path)
        assert not db_path.exists()
    finally:
        config["engine"].dispose()


@pytest.mark.parametrize("handler_fails", [False, True])
def test_get_db_closes_the_session(monkeypatch, handler_fails):
    session = Mock()
    session_factory = Mock(return_value=session)
    monkeypatch.setattr(database, "SessionLocal", session_factory)
    dependency = database.get_db()

    assert next(dependency) is session
    if handler_fails:
        error = RuntimeError("handler failed")
        with pytest.raises(RuntimeError) as exc:
            dependency.throw(error)
        assert exc.value is error
    else:
        with pytest.raises(StopIteration):
            next(dependency)

    session_factory.assert_called_once_with()
    session.close.assert_called_once_with()
