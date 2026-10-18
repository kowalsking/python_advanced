from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic, Protocol

T = TypeVar('T', bound=Identifieble) # <- bound
R = TypeVar('R')

@dataclass
class Identifieble(Protocol):
    id: int
    
def get_by_id(items: list[T], id_: int) -> Optional[T]:
    for item in items:
        if item.id == id_:
            return item
        return None

@dataclass
class User(Generic[T]):
    id: int
    
@dataclass
class Product(Generic[T]):
    ids: int
    
@dataclass
class Order(Generic[T]):
    id: int
    
get_by_id([User(1)], 1)
get_by_id([Product(1)], 1) # error