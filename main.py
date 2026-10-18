from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic

T = TypeVar('T')
R = TypeVar('R')

@dataclass
class Repository(Generic[T]):
    items: list[T]
    
    def add(self, item: T):
        self.items.append(item)

    def get_by_index(self, index: int) -> Optional[T]:
        if 0 <= index <= len(self.items):
            return self.items[index]
        return None
    
    def get_all(self) -> list[T]:
        return self.items

repo = Repository[int]([1, 2])
print(repo.get_by_index(1))