"""Provide SQL clauses."""

from string import Template
from typing_extensions import LiteralString


def AVG(field: str) -> LiteralString:
    """Provide average of integers."""
    return Template('AVG($field)').substitute(field=field)


def COUNT(field: str = '*') -> LiteralString:
    """Provide count SQL expression."""
    return Template('COUNT($field)').substitute(field=field)


def LEN(field: str) -> LiteralString:
    """Provide summing SQL expression."""
    return Template('LEN($field)').substitute(field=field)


def MAX(field: str) -> LiteralString:
    """Provide maximum SQL statement."""
    return Template('MAX($field)').substitute(field=field)


def MIN(field: str) -> LiteralString:
    """Provide minimun SQL statement."""
    return Template('MIN($field)').substitute(field=field)


def SUM(field: str) -> LiteralString:
    """Provide SQL statement for summing SQL field."""
    return Template('SUM($field)').substitute(field=field)


def UPPER(field: str) -> LiteralString:
    """Provide SQL statement to convert string to uppercase."""
    return Template('UPPER($field)').substitute(field=field)


__all__ = ['AVG', 'COUNT', 'LEN', 'MAX', 'MIN', 'SUM', 'UPPER']
