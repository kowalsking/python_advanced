class Order:
    def __init__(self, number: int, total: float):
        self.number = number
        self.total = total
        print(f"Order created: {number} with sum {total}")
    
    def process(self):
        print('Order is done!')

class EmailOrder(Order):
    def __init__(self, number: int, total: float, email: str):
        # super().__init__(number, total)
        self.email = email
    
    def process(self):
        print('Message is sent')
        super().process()
        

email = EmailOrder(10, 2, 'a@a.com')
email.process()