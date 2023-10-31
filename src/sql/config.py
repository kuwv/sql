"""SQL default configuration."""

from enum import Enum


class FormatCodes(Enum):
    """Provide ANSI C printf format codes."""

    character = '%c'  # a single character
    decimal = '%d'  # a decimal integer (assumes base 10)
    exponent = '%e'  # a floating point number in scientific notation
    floating_point = '%f'  # a floating point number for floats
    octal = '%o'  # an octal (base 8) integer
    integer = '%i'  # a decimal integer (detects the base automatically)
    string = '%s'  # a string
    unsigned = '%u'  # int unsigned decimal

    # %hi  short (signed)
    # %hu  short (unsigned)
    # %Lf  long double
    # %n  prints nothing
    # %x  a hexadecimal (base 16) integer
    # %p  an address (or pointer)
    # %E  a floating point number in scientific notation
    # %%  the % symbol


class Paramstyle(Enum):
    """Provide PEP249 parameter style arguments."""

    format_codes = FormatCodes
    named = ':name'
    numeric = ':1'
    pystyle = '%(name)s'
    qmark = '?'


paramstyle = 'any'
