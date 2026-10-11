class Notification:
    def __init__(self, sender):
        self.sender = sender
    
    def send(self, message):
        self.sender.send(message)
    
class EmailSender:
    def send(self, message):
        print(f'Send by email: {message}')
    
noti = Notification(EmailSender())

noti.send("Heello!!!ww")