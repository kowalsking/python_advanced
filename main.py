from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic

T = TypeVar('T')
R = TypeVar('R')

@dataclass
class IntBox:
    value: int
    
    def get(self) -> int:
        return self.value
    

@dataclass
class Box(Generic[T]):
    value: T
    
    def get(self) -> T:
        return self.value
    
int_box = Box(1)
print(int_box.get())
str_box = Box('hello')