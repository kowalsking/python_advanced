from dataclasses import dataclass


@dataclass
class User:
    name: str
    bonus: int = 0
    
    def add_bonus(self, amount: int):
        self.bonus += amount
        print(f'{self.name} get {amount} bonuses. All: {self.bonus}')

class PremiumUser(User):
    def add_bonus(self, amount: int):
        self.bonus += amount * 2
        print(f'{self.name} get {amount} bonuses. All: {self.bonus}')
        
class BannedUser(User):
    def add_bonus(self, amount: int):
        # raise Exception('Banned User!')
        print(f'{self.name} can"t get bonuses.')

user = User('A')