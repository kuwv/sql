"""Provide Data Manipulation Language fields."""

from typing import Any, Optional

from sql.utils import FluentMixin


class SELECT(FluentMixin):
    """Select clause for SQL fields."""

    handlers = ['FROM']

    def __init__(self, *fields: Any) -> None:
        if fields and isinstance(fields[0], FluentMixin):
            template = '$statement SELECT $fields'
            self.data = {'statement': fields[0]}
        else:
            template = 'SELECT $fields'
            self.data = {
                'statement': None,
                'fields': '*' if not fields else ', '.join(fields),
            }
        super().__init__(template)

    def __call__(self, *fields: Any) -> Any:
        self.data['fields'] = '*' if not fields else ', '.join(fields)
        return self


class SELECT_ALL(FluentMixin):
    """Select clause for SQL fields."""

    handlers = ['FROM']

    def __init__(self, *fields: Any) -> None:
        if fields and isinstance(fields[0], FluentMixin):
            template = '$statement SELECT ALL $fields'
            self.data = {'statement': fields[0]}
        else:
            template = 'SELECT ALL $fields'
            self.data = {
                'statement': None,
                'fields': '*' if not fields else ', '.join(fields),
            }
        super().__init__(template)

    def __call__(self, *fields: Any) -> Any:
        self.data['fields'] = '*' if not fields else ', '.join(fields)
        return self


class SELECT_DISTINCT(FluentMixin):
    """Select clause for SQL fields."""

    fields: Optional[Any]
    statement: Optional[Any]
    handlers = ['FROM']

    def __init__(self, *fields: Any) -> None:
        if fields and isinstance(fields[0], FluentMixin):
            template = '$statement SELECT DISTINCT $fields'
            self.data = {'statement': fields[0]}
        else:
            template = 'SELECT DISTINCT $fields'
            self.data = {
                'statement': None,
                'fields': '*' if not fields else ', '.join(fields),
            }
        super().__init__(template)

    def __call__(self, *fields: Any) -> Any:
        self.data['fields'] = '*' if not fields else ', '.join(fields)
        return self


# SELECT_INTO
# SELECT_TOP

# AVG
# INTO
# SUM
# TOP

_all_ = ['SELECT', 'SELECT_ALL', 'SELECT_DESTINCT']
