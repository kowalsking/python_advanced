class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        
    def get_info(self):
        return f"{self.email}, {self.email}"

class Student(User): 
    def watch_video(self):
        print('Watching...')


class Mentor(User):
    def check_homework(self):
        print('Checking...')
        

student = Student('Dima', 'king@wazar.ai')
print(student.get_info())
print(student.email)