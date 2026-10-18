from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic, Protocol

T = TypeVar('T', bound=Runnable) # <- bound
R = TypeVar('R')

class Runnable(Protocol):
    def run(self) -> None: ...

@dataclass
class TaskRunner(Generic[T]):
    tasks: list[T]

    def run_all(self) -> None:
        for task in self.tasks:
            task.run()