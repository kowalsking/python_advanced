from typing import Any

class Demo:
    def __getattribute__(self, name: str) -> Any:
        print(f'Ac: {name}')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f'{name} not found')
        return None
    
    def hello(self):
        print('hello', self)
    
    
d = Demo()
d.x = 42
print(d.x)
print(d.y)

print(d.__dict__)
print(d.hello)
print(Demo.hello)