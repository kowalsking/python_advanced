from typing import TypeVar, Callable


T = TypeVar('T')
R = TypeVar('R')

def make_pair(a: T, b: R) -> tuple[T, R]:
    return (a, b)

def get_first(a: tuple[T, R]) -> T:
    return a[0]

def get_second(a: tuple[T, R]) -> R:
    return a[1]

def swap_pair(a: tuple[T, R]) -> tuple[R, T]:
    return (a[1], a[0])