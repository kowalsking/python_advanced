from dataclasses import dataclass, field
from datetime import datetime

@dataclass(order=True)
class Task:
    title: str
    secret_key: str = field(repr=False, compare=False)
    priority: int = 3
    done: bool = False
    created_at: datetime | None = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
task_1 = Task('make lesson', 'secret')
task_2 = Task('make lesson', 'secret')
print(task_1)