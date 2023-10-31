"""Provide Data Manipulation Language statements."""

import importlib
import inspect
from abc import ABC, abstractmethod  # noqa
from functools import partial
from string import Template
from typing import Any, Dict, Callable, Optional
from typing_extensions import LiteralString


class FluentMixin(Template):
    """Provide fluent API to SQL clauses using chain of responisibily."""

    data: Dict[LiteralString, Any]

    def _(self, name: str, /, *args: Any, **kwargs: Any) -> 'FluentMixin':
        if (
            hasattr(self.__class__, 'handlers')
            and name in self.__class__.handlers
        ):
            # import only modules within scope to prevent unintended imports
            # frm = inspect.stack()[2]
            # module = inspect.getmodule(frm[0])
            # if module and module.__name__ == '__main__':
            #     # handle local script imports

            module = importlib.import_module('sql')
            cls = getattr(module, name.upper())

            # attr = getattr(module, name.upper())
            # if callable(attr):
            #     def wrapper(*args: Any, **kwargs: Any) -> Any:
            #         """Call query for statment."""
            #         return attr(self, *args, **kwargs)
            #     return wrapper
            # return attr

            return cls(self, *args, **kwargs)
        raise KeyError(
            f"incorrect clause '{name}' called from '{self.__class__}'"
        )

    @staticmethod
    def _isclass(value: Any) -> bool:
        return inspect.isclass(value)

    def __getattr__(self, name: str) -> Any:
        return self._(name)

    def __str__(self) -> str:
        return self.substitute(**self.data)


class Infix:
    """Provide infix operators for SQL expresions."""

    def __init__(self, fn: Callable) -> None:
        self.__fn = fn

    def __call__(self, left: Any, right: Any) -> Any:
        return self.__fn(left, right)

    def __or__(self, other: Any) -> str:
        return self.__fn(other)

    def __ror__(self, other: Any) -> 'Infix':
        return Infix(partial(self.__fn, other))


class Validator(ABC):
    """Provide abstract validation descriptor."""

    __name: str

    def __set_name__(self, obj: object, name: str) -> None:
        self.__name = f"_{name}"

    def __get__(
        self, obj: object, objtype: Optional[type[object]] = None
    ) -> str:
        return getattr(obj, self.__name)

    def __set__(self, obj: object, value: Any) -> None:
        self.validate(value)
        setattr(obj, self.__name, value)

    @abstractmethod
    def validate(self, value: Any) -> None:
        """Provide validation interface."""
