from dataclasses import dataclass
from typing import Callable, TypeVar, Optional

T = TypeVar('T')
R = TypeVar('R')

def safe_get(arr: list[T], index: int) -> Optional[T]:
    if 0 <= index <= len(arr):
        return arr[index]
    return None

def map_optional(value: Optional[T], transformer: Callable[[T], R]) -> Optional[R]:
    if value is not None:
        transformer(value)
    return None

def or_else(value: Optional[T], default: T) -> T:
    if value is not None:
        return value
    return default


print(safe_get([1, 2, 3], 10))
