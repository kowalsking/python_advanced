from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class StockRepository(Protocol):
    def get_stock_count(self) -> int: ...

class Notifier(Protocol):
    def notify(self, message: str): ...

@dataclass
class InMemoryStockRepository:
    items_count: int

    def get_stock_count(self) -> int:
        return self.items_count
    
class EmailNotifier:
    def notify(self, message: str):
        print(f'Email: {message}')

@dataclass
class LowStockService:
    repository: StockRepository
    notifier: Notifier
    
    def run(self):
        c = self.repository.get_stock_count()
        if c <= 10:
            self.notifier.notify('Buy more items')
        else:
            print('All good!')

service = LowStockService(InMemoryStockRepository(101), EmailNotifier())
service.run()
