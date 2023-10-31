"""Provide Data Manipulation Language statements."""

from typing import Any, Optional
from typing_extensions import LiteralString

from .dql import SELECT  # noqa
from .utils import FluentMixin


class DELETE(FluentMixin):
    """Delete data from a table."""

    handlers = ['FROM']

    def __init__(self, statement: Optional[Any] = None) -> None:
        super().__init__('$statement DELETE' if statement else 'DELETE')
        self.data = {'statement': statement}

    def __call__(self) -> Any:
        return self


class INSERT_INTO(FluentMixin):
    """Insert data into a table."""

    handlers = ['ALL', 'ANY', 'DISTINCT', 'FROM', 'SELECT', 'TOP', 'VALUES']

    def __init__(self, table: Any, columns: Optional[Any] = None) -> None:
        super().__init__(
            'INSERT INTO $table ($columns)'
            if columns
            else 'INSERT INTO $table'
        )
        self.data = {
            'table': table,
            'columns': None if not columns else ', '.join(columns),
        }


class UPDATE(FluentMixin):
    """Update data within a table."""

    handlers = ['SET']

    def __init__(self, table: Any) -> None:
        super().__init__('UPDATE $table')
        self.data = {
            'table': table.__name__ if self._isclass(table) else table
        }


__all__ = ['DELETE', 'INSERT_INTO', 'UPDATE']
