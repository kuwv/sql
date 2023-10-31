"""Provide SQL clauses."""

from inspect import isclass
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
class EQUALS(Template):
    """Provide equivilance SQL expersion."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left = $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class GREATER_EQUAL(Template):
    """Provide equivilance SQL expersion."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left >= $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class GREATER_THAN(Template):
    """Provide equivilance SQL expersion."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left > $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class LESS_EQUAL(Template):
    """Provide equivilance SQL expersion."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left <= $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class LESS_THAN(Template):
    """Provide equivilance SQL expersion."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left < $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


@Infix
class NOT_EQUAL(Template):
    """Combine multiple seleciton clauses."""

    def __init__(self, left: LiteralString, right: LiteralString) -> None:
        super().__init__('$left <> $right')
        self.__left = left.__name__ if isclass(left) else left
        self.__right = right

    def __str__(self) -> LiteralString:
        return self.substitute(left=self.__left, right=self.__right)


EQ = EQUALS
GE = GREATER_EQUAL
GT = GREATER_THAN
LE = LESS_EQUAL
LT = LESS_THAN
NE = NOT_EQUAL

__all__ = [
    'EQ',
    'EQUALS',
    'GE',
    'GT',
    'LE',
    'LT',
    'NE',
]
