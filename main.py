from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic, Protocol, Union, TypeGuard

T = TypeVar('T')
R = TypeVar('R')

def is_int_list(x: list[int] | list[str]) -> TypeGuard[list[int]]:
    return all(isinstance(i, int) for i in x)

def f(xs: list[int] | list[str]):
    if is_int_list(xs):
        xs[0].is_integer()
    else:
        xs[0].capitalize() # error
