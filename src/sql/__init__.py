# :copyright: (c) 2023 by Jesse Johnson.
# :license: Apache 2.0, see LICENSE for more details.

"""Fluent SQL in Python."""

import logging

from typing import Any, List

from ._clauses import *  # noqa
from ._functions import *  # noqa
from ._operators import *  # noqa
from .dcl import *  # noqa
from .ddl import *  # noqa
from .ddl.assign import *  # noqa
from .dml import *  # noqa
from .dql import *  # noqa
from .tcl import *  # noqa
from .utils import FluentMixin

__author__ = 'Jesse P. Johnson'
__author_email__ = 'jpj6652@gmail.com'
__title__ = 'sql'
__description__ = 'Inspection based parser built on argparse.'
__version__ = '0.1.0a0'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023 Jesse Johnson.'
# __all__: List[str] = []

logging.getLogger(__name__).addHandler(logging.NullHandler())


class END(FluentMixin):
    """Select clause for SQL statement."""

    def __init__(self, statement: Any) -> None:
        super().__init__('$statement;')
        self.__statement = str(statement)

    def __call__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.substitute(statement=self.__statement)

    @property
    def handlers(self) -> List[str]:
        """Return valid handler chain."""
        return []
