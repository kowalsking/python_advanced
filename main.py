from dataclasses import dataclass
from typing import TypeVar, Optional


@dataclass
class User:
    id: int
    name: str
    email: str
    
def get_user_by_id(user_id: int) -> Optional[User]:
    users = [
        User(1, 'Anton', 'a@a.ua'),
        User(2, 'Vasia', 'v@a.ua'),
    ]
    
    for user in users:
        if user.id == user_id:
            return user
    return None

user = get_user_by_id(999)
