from typing import TypeVar, Callable


T = TypeVar('T')
R = TypeVar('R')

def proccess_items(items: list[T], transformer: Callable[[T], R]) -> list[R]:
    return [transformer(item) for item in items]

def to_upper(s: str) -> str:
    return s.upper()

result = proccess_items(['Anton', 'Vasia'], to_upper)