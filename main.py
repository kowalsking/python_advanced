from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic

Number = TypeVar('Number', int, float) # <- type limitation
R = TypeVar('R')

@dataclass
class MyMath(Generic[Number]):
    def max(self, a: Number, b: Number):
        return a if a > b else b
    
    def add(self, a: Number, b: Number):
        return a + b
    
    
math = MyMath[int]()