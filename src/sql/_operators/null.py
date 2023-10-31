"""Provide SQL NULL clauses."""

from typing_extensions import LiteralString

from ..utils import FluentMixin


class IS_NULL(FluentMixin):
    """Combine multiple seleciton clauses."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement IS NULL')
        self.data = {'statement': statement}

    def __call__(self) -> 'IS_NULL':
        return self


class IS_NOT_NULL(FluentMixin):
    """Provide equivilance SQL expersion."""

    handlers = ['END']

    def __init__(self, statement: LiteralString) -> None:
        super().__init__('$statement IS NOT NULL')
        self.data = {'statement': statement}

    def __call__(self) -> 'IS_NOT_NULL':
        return self


__all__ = ['IS_NULL', 'IS_NOT_NULL']
