from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    qty: int = 1
    
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        
    def subtotal(self):
        return self.price * self.qty
    
class NoDiscount:
    def discount(self, total: float) -> float:
        return 0

@dataclass
class PercentageDiscount:
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100)

@dataclass
class Order:
    def __init__(self, items: list[Item], policy):
        self.items = items
        self.policy = policy
    
    def total(self):
        return sum(i.subtotal() for i in self.items)
    
    def total_with_discount(self):
        t = self.total()
        return t - self.policy.discount(t)
    
    def set_policy(self, policy):
        self.policy = policy

basket = [Item('Paper', 100, 5), Item('Candy', 20, 1)]
order = Order(basket, NoDiscount())
print(order.total())
print(order.total_with_discount())

order.set_policy(PercentageDiscount(10))
print(order.total())
print(order.total_with_discount())