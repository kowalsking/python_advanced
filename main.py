from dataclasses import dataclass


@dataclass
class Order:
    items: list[str]

    def calculate_total(self):
        return 1
    
class OrderRepository:
    def save_to_db(self, order: Order):
        print('Saved to DB')

class EmailService:
    def sent_conf_email(self, email: str):
        print('email sent')