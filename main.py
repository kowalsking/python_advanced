class CreditMixin:
    price = 0
    length = 0
    
    def calculate_credit(self):
        return self.price / self.length

class Course:
    def __init__(self, name: str, price: float, lenght: int):
        self.name = name
        self.price = price
        self.length = lenght
    
    def get_price(self):
        return self.price
    
    def get_info(self):
        return f'info about course: {self.name}'

class AICourse(Course, CreditMixin):
    pass
    
class ProjectCourse(Course, CreditMixin):
    def __init__(self, name: str, price: float, length: int, project_name: str):
        super().__init__(name, price, length)
        self.project_name = project_name
    
    def get_project_info(self):
        return f'Project: {self.project_name}'
    
course = ProjectCourse('Python', 10000, 2, 'Calculus')
print(course.get_info())
print(course.get_project_info())
print(course.calculate_credit())