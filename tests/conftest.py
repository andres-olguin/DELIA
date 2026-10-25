import sqlalchemy
from sqlalchemy.pool import StaticPool

# app.database crea el engine de PostgreSQL al importarse y main.py conecta ahí;
# se sustituye por SQLite en memoria antes de importar la app.
_real_create_engine = sqlalchemy.create_engine
sqlalchemy.create_engine = lambda *a, **k: _real_create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
