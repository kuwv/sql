"""Provide SQL clauses for sorting results."""

from typing_extensions import LiteralString

from ..utils import FluentMixin


class GROUP_BY(FluentMixin):
    """GROUP BY selection by match selector."""

    handlers = ['END', 'HAVING', 'ORDER_BY']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement GROUP BY $column')
        self.data = {'statement': statement}

    def __call__(self, column: LiteralString) -> 'GROUP_BY':
        self.data['column'] = column
        return self


class HAVING(FluentMixin):
    """GROUP BY selection by match selector."""

    handlers = ['END', 'ORDER_BY']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement HAVING $condition')
        self.data = {'statement': statement}

    def __call__(self, condition: LiteralString) -> 'HAVING':
        self.data['condition'] = condition
        return self


class ORDER_BY(FluentMixin):
    """ORDER BY selection by selector."""

    handlers = ['ASC', 'DESC', 'END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement ORDER BY $column')
        self.data = {'statement': statement}

    def __call__(self, column: LiteralString) -> 'ORDER_BY':
        self.data['column'] = column
        return self


class ASC(FluentMixin):
    """Sort ascending clause for ORDER BY statement."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement ASC')
        self.data = {'statement': str(statement)}

    def __call__(self) -> 'ASC':
        return self


class DESC(FluentMixin):
    """Sort descending clause for ORDER BY statement."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement DESC')
        self.data = {'statement': str(statement)}

    def __call__(self) -> 'DESC':
        return self


__all__ = [
    'ASC',
    'DESC',
    'GROUP_BY',
    'HAVING',
    'ORDER_BY',
]
