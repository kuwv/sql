"""Provide Data Definition Language capabilities."""

from typing import Tuple
from typing_extensions import LiteralString

from ..utils import FluentMixin


class ALTER_DATABASE(FluentMixin):
    """Alter the structure of a database."""

    handlers = ['OWNER_TO', 'RENAME_TO', 'RESET', 'SET']

    def __init__(self, database: LiteralString, /) -> None:
        super().__init__('ALTER DATABASE $database')
        self.data = {'database': database}


class ALTER_TABLE(FluentMixin):
    """Alter the structure of a database."""

    handlers = ['ADD']

    def __init__(self, table: LiteralString, /) -> None:
        super().__init__('ALTER TABLE $table')
        self.data = {'table': table}


class ALTER_SCHEMA(FluentMixin):
    """Alter the structure of a database."""

    handlers = ['RENAME_TO', 'OWNER_TO']

    def __init__(self, database: LiteralString, /) -> None:
        super().__init__('ALTER SCHEMA $database')
        self.data = {'database': database}


# class COMMENT(FluentMixin):
#     """Add comments to a data dictionary."""


class CREATE_DATABASE(FluentMixin):
    """Create a database."""

    handlers = ['END', 'FROM']

    def __init__(self, database: LiteralString, /) -> None:
        super().__init__('CREATE DATABASE $database')
        self.data = {'database': database}


class CREATE_SCHEMA(FluentMixin):
    """Create a database table."""

    handlers = ['AUTHORIZATION', 'END', 'IF']

    def __init__(
        self, schema: LiteralString, columns: Tuple[LiteralString], /
    ) -> None:
        super().__init__('CREATE SCEHMA $schema (${columns})')
        self.data = {'schema': schema, 'columns': ', '.join(columns)}


class CREATE_TABLE(FluentMixin):
    """Create a database table."""

    handlers = ['AS', 'END']

    def __init__(
        self, table: LiteralString, columns: Tuple[LiteralString], /
    ) -> None:
        super().__init__('CREATE TABLE $table (${columns})')
        self.data = {'table': table, 'columns': ', '.join(columns)}


class CREATE_VIEW(FluentMixin):
    """Create a database view."""

    handlers = ['AS']

    def __init__(
        self, view: LiteralString, columns: Tuple[LiteralString], /
    ) -> None:
        super().__init__('CREATE VIEW $view (${columns})')
        self.data = {'view': view, 'columns': ', '.join(columns)}


class DROP_DATABASE(FluentMixin):
    """Drop a database."""

    handlers = ['END', 'IF']

    def __init__(self, database: LiteralString, /) -> None:
        super().__init__('DROP DATABASE $database')
        self.data = {'database': database}


class DROP_COLUMN(FluentMixin):
    """Drop a database."""

    handlers = ['END', 'IF']

    def __init__(self, database: LiteralString, /) -> None:
        super().__init__('DROP COLUMN $database')
        self.data = {'database': database}


class DROP_SCHEMA(FluentMixin):
    """Drop table from a database."""

    handlers = ['END', 'IF']

    def __init__(self, schema: LiteralString, /) -> None:
        super().__init__('DROP SCHEMA $schema')
        self.data = {'schema': schema}


class DROP_TABLE(FluentMixin):
    """Drop table from a database."""

    handlers = ['END', 'IF']

    def __init__(self, table: LiteralString, /) -> None:
        super().__init__('DROP TABLE $view')
        self.data = {'table': table}


class DROP_VIEW(FluentMixin):
    """Drop view from a database."""

    handlers = ['END', 'IF']

    def __init__(self, view: LiteralString, /) -> None:
        super().__init__('DROP TABLE $view')
        self.data = {'view': view}


# class RENAME(FluentMixin):
#     """Rename objects within a database."""


# class TRUNCATE(FluentMixin):
#     """Remove all recored from a table within a database."""


__all__ = [
    'ALTER_DATABASE',
    # 'COMMENT',
    'CREATE_DATABASE',
    'CREATE_TABLE',
    'CREATE_VIEW',
    'DROP_DATABASE',
    'DROP_TABLE',
    'DROP_VIEW',
    # 'RENAME',
    # 'TRUNCATE',
]
