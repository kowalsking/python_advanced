class User:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Amount should be positive')
    
    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else: 
            raise ValueError('No enought money!')
        
u = User('Tony', 1000)
u.deposit(123)

print(u.get_balance())

u.withdraw(344)
u._User__balance = -1 # Так можна
u.__balance = -1 # Створить оремиу змінну __balance
print(u.get_balance())
print(u.__dict__)