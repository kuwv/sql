"""Provide SQL clauses."""

from typing import Any
from typing_extensions import LiteralString

from ..utils import FluentMixin


class AS(FluentMixin):
    """Provide from clause for SQL statements."""

    handlers = ['WHERE']

    def __init__(self, statement: LiteralString, /) -> None:
        super().__init__('$statement AS $alias')
        self.data = {'statement': statement}

    def __call__(self, alias: Any, /) -> Any:
        self.data['alias'] = alias.__name__ if self._isclass(alias) else alias
        return self


class SET(FluentMixin):
    """Provide from clause for SQL statements."""

    handlers = ['WHERE']  # , 'INNER', 'OUTER', 'UNION']

    def __init__(self, statement: LiteralString, /) -> None:
        super().__init__('$statement SET $fields')
        self.data = {'statement': statement}

    def __call__(self, *fields: Any) -> Any:
        self.data['fields'] = ', '.join([str(x) for x in fields])
        return self


__all__ = ['AS', 'SET']
