class Positive:
    def __init__(self, name):
        self.name = name
        
    def __get__(self, obj, owner):
        print('get')
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        print('set')
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Product:
    price = Positive("price")


p = Product()
p.price = -100
print(p.price)
