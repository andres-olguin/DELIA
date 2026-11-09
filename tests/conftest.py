"""Keep all pytest database tests isolated from production credentials.

The SQLAlchemy model tests create/drop SQLite tables in a private in-memory
connection. No monkeypatching the global sqlalchemy engine constructor.
"""
import os

os.environ["DANREXO_DATABASE_URL"] = "sqlite://"
