class Payment:
    def pay(self, amount):
        raise NotImplementedError('Methond should exist!')

class CardPayment(Payment):
    def pay(self, amount):
        print(f'Payed by card: {amount}')

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f'Payed by crypto: {amount}')

class ApplePayment(Payment):
    def pay(self, amount):
        print(f'Payed by ApplyPay: {amount}')

payments = [CardPayment(), CryptoPayment(), ApplePayment()]

for p in payments:
    p.pay(100)