# class Notifier:
#     def send(self, message: str, method: str) -> None:
#         if method == 'email':
#             print(f'[Email] Message sent: {message}')
#         elif method == 'push':
#             print(f'[Push] Message sent: {message}')
#         else:
#             print('Unknown notification method.')


from abc import ABC, abstractmethod
from dataclasses import dataclass


class NotificationPolicy(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
    
class EmailNotification(NotificationPolicy):
    def send(self, message: str) -> None:
        print(f'[Email] Message sent: {message}')

class PushNotification(NotificationPolicy):
    def send(self, message: str) -> None:
        print(f'[Push] Message sent: {message}')

class TelegramNotification(NotificationPolicy):
    def send(self, message: str) -> None:
        print(f'[Telegram] Message sent: {message}')

@dataclass
class Notifier:
    notifier: NotificationPolicy
    
    def send(self, message: str) -> None:
        self.notifier.send(message)
    
calc = Notifier(TelegramNotification())
print(calc.send('Hello'))