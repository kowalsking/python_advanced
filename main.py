from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic, Protocol, Union

T = TypeVar('T')
R = TypeVar('R')

# def safe_div(a: float, b: float) -> Union[float, str]:
def safe_div(a: float, b: float) -> float | str:
    if b == 0:
        return 'divide on 0'
    return a / b

def ensure_list(value: T | list[T]) -> list[T]:
    if isinstance(value, list):
        return value
    return [value]

