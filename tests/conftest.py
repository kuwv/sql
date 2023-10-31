"""Configure PyTest integration tests."""

from sqlite3 import Connection, Cursor
from typing import Generator

import pytest


@pytest.fixture
def cursor() -> Generator[Cursor, None, None]:
    """Create SQLite3 database instance for tests."""
    with Connection(':memory:') as connection:
        yield connection.cursor()
