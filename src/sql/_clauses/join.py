"""Provide SQL clauses."""

from typing import Any
from typing_extensions import LiteralString

from ..utils import FluentMixin


class INNER_JOIN(FluentMixin):
    """Provide INNER JOIN clause for SQL statements."""

    handlers = ['ON']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement INNER JOIN $table')
        self.data = {'statement': statement}

    def __call__(self, table: LiteralString) -> Any:
        self.data['table'] = table
        return self


class LEFT_JOIN(FluentMixin):
    """Provide LEFT OUTER JOIN clause for SQL statements."""

    handlers = ['ON']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement LEFT JOIN $table')
        self.data = {'statement': statement}

    def __call__(self, table: LiteralString) -> Any:
        self.data['table'] = table
        return self


class RIGHT_JOIN(FluentMixin):
    """Provide RIGHT OUTER JOIN clause for SQL statements."""

    handlers = ['ON']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement RIGHT JOIN $table')
        self.data = {'statement': statement}

    def __call__(self, table: LiteralString) -> Any:
        self.data['table'] = table
        return self


class FULL_JOIN(FluentMixin):
    """Provide FULL OUTER JOIN clause for SQL statements."""

    __table: LiteralString
    handlers = ['ON']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement FULL JOIN $table')
        self.data = {'statement': statement}

    def __call__(self, table: LiteralString) -> Any:
        self.data['table'] = table
        return self


class ON(FluentMixin):
    """Provide ON clause for SQL JOIN statements."""

    __values: LiteralString
    handlers = ['END', 'WHERE']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement ON $values')
        self.data = {'statement': statement}

    def __call__(self, values: Any) -> Any:
        self.data['values'] = (
            values.__name__ if self._isclass(values) else values
        )
        return self


__all__ = ['INNER_JOIN', 'LEFT_JOIN', 'RIGHT_JOIN', 'FULL_JOIN', 'ON']
