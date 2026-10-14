from abc import ABC, abstractmethod
from dataclasses import dataclass


class Logger(ABC):
    @abstractmethod
    def log(self, message): ...

class FileLogger(Logger):
    def log(self, message: str):
        print(f'Write file: {message}')
        
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f'Write file: {message}')

@dataclass
class UserService:
    logger: Logger

    def create_user(self, name: str):
        self.logger.log(f'Created account {name}')

service = UserService(ConsoleLogger())
service.create_user('sd')