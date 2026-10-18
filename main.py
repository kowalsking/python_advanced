from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic, Protocol, Union, TypeGuard

T = TypeVar('T')
R = TypeVar('R')

@dataclass
class ClickEvent:
    x: int
    y: int
    
@dataclass
class KeyEvent:
    key: str
    
@dataclass
class ResizeEvent:
    width: int
    height: int
        
def handle_event(ev: ClickEvent | KeyEvent | ResizeEvent) -> str:
    match ev:
        case ClickEvent(x=x, y=y):
            return f"Click: {x}, {y}"
        case KeyEvent(key=k):
            return f"Pressed on {k}"
        case ResizeEvent(width=w, height=h):
            return f"Resized to {w}x{h}"
    raise ValueError('Unknown event')

print(handle_event(ClickEvent(1, 10)))
print(handle_event(KeyEvent('Enter')))
print(handle_event(ResizeEvent(1920, 1080)))
