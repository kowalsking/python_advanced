from abc import ABC, abstractmethod
from dataclasses import dataclass


# @dataclass
class Payment:
    def pay(self, amount: float) -> float:
        print(f'P: {amount}')
        return amount

@dataclass
class BonusPayment(Payment):
    bonuses: float
    def pay(self, amount: float) -> float:
        final = amount - self.bonuses
        print(f'P: {final}')
        return final

@dataclass
class InstallmentPayment(Payment):
    part: int
    def pay(self, amount: float) -> float:
        final = amount / self.part
        print(f'P: {amount / self.part}')
        return final
    
    
def pay(method: Payment):
    return method.pay(33)

pay(InstallmentPayment(2))