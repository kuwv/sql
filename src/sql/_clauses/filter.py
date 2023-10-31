"""Provide SQL clauses."""

from typing import Any, Tuple
from typing_extensions import LiteralString

from ..utils import FluentMixin


class FROM(FluentMixin):
    """Provide from clause for SQL statements."""

    handlers = [
        'AS',
        'END',
        'INNER_JOIN',
        'FULL_JOIN',
        'LEFT_JOIN',
        'RIGHT_JOIN',
        'GROUP_BY',
        'ORDER_BY',
        'WHERE',
        'UNION',
    ]

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement FROM $table')
        self.data = {'statement': statement}

    def __call__(self, table: Any) -> Any:
        self.data['table'] = table.__name__ if self._isclass(table) else table
        return self


class BETWEEN(FluentMixin):
    """Combine multiple seleciton clauses."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement BETWEEN $condition')
        self.data = {'statement': statement}

    def __call__(self, condition: Any) -> 'BETWEEN':
        if ' AND ' not in str(condition):
            raise Exception('BETWEEN statement missing AND condition')
        self.data['condition'] = condition
        return self


class IN(FluentMixin):
    """Combine multiple seleciton clauses."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement IN (${fields})')
        self.data = {'statement': statement}

    def __call__(self, *fields: Any) -> 'IN':
        self.data['fields'] = ', '.join(fields)
        return self


class NOT(FluentMixin):
    """Combine multiple seleciton clauses."""

    handlers = ['BETWEEN', 'IN', 'END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement NOT IN (${fields})')
        self.data = {'statement': statement}

    def __call__(self, *fields: Any) -> 'NOT':
        self.data['fields'] = ', '.join(fields)
        return self


class LIMIT(FluentMixin):
    """Provide from clause for SQL statements."""

    handlers = ['WHERE', 'INNER_JOIN', 'OUTER', 'UNION']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('LIMIT $statement')
        self.data = {'statement': statement}

    def __call__(self, table: Any) -> Any:
        self.data['table'] = table.__name__
        return self


class WHERE(FluentMixin):
    """Provide where clause for SQL statements."""

    handlers = [
        'ANY',
        'ALL',
        'BETWEEN',
        'EXISTS',
        'IN',
        'NOT',
        'GROUP_BY',
        'ORDER_BY',
        'EXECUTE',
        'END',
    ]

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement WHERE $condition')
        self.data = {'statement': statement}

    def __call__(self, condition: LiteralString) -> Any:
        self.data['condition'] = condition
        return self


class VALUES(FluentMixin):
    """Provide where clause for SQL statements."""

    handlers = [
        'ANY',
        'ALL',
        'EXISTS',
        'GROUP_BY',
        'ORDER_BY',
        'EXECUTE',
        'END',
    ]

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement VALUES (${values})')
        self.data = {'statement': statement}

    def __call__(self, *values: Any) -> Any:
        self.data['values'] = (', ').join(values)
        return self


# WHERE CURRENT OF clause

__all__ = [
    'BETWEEN',
    'FROM',
    'IN',
    'NOT',
    'LIMIT',
    'WHERE',
    'VALUES',
]
