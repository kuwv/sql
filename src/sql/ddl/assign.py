"""Provide SQL clauses."""

from typing import Any
from typing_extensions import LiteralString

from ..utils import FluentMixin


class ADD(FluentMixin):
    """Provide from clause for SQL statements."""

    handlers = ['WHERE']

    def __init__(self, statement: LiteralString, /) -> None:
        super().__init__('$statement ADD $column $datatype')
        self.data = {'statement': statement}

    def __call__(
        self, column: LiteralString, datatype: LiteralString, /
    ) -> Any:
        self.data['column'] = column
        self.data['datatype'] = datatype
        return self


class RENAME_TO(FluentMixin):
    """Provide from clause for SQL statements."""

    __name: LiteralString
    handlers = ['END']  # , 'INNER', 'OUTER', 'UNION']

    def __init__(self, statement: LiteralString, /) -> None:
        super().__init__('$statement RENAME TO $name')
        self.data = {'statement': statement}

    def __call__(self, name: LiteralString, /) -> Any:
        self.data['name'] = name
        return self


__all__ = ['ADD', 'RENAME_TO']
