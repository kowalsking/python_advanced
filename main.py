class User:
    users = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        User.users.append(self)
        
    @classmethod
    def from_string(cls, data: str):
        name, age = data.split(',')
        return cls(name, int(age))

    @classmethod
    def total_users(cls):
        return len(cls.users)
    
edward = User('Edward', 23)
kate = User('Kate', 32)
print(User.total_users())

anna = User.from_string('Anna,52')

print(anna.name)
print(anna.age)