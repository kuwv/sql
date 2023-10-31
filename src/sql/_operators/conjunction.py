"""Provide SQL clauses."""

from string import Template
from typing_extensions import LiteralString

from ..utils import Infix

# BETWEEN
# ALL
# ANY
# SOME
# LIKE
# IN
# NULL


@Infix
class AND(Template):
    """Combine multiple seleciton clauses."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left AND $right')
        self.__left = left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class OR(Template):
    """Combine multiple seleciton clauses."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left OR $right')
        self.__left = left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


__all__ = ['AND', 'OR']
