from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: float

# @dataclass
class StudentsList:
    all_students: list[Student] = []

    def add_student(self, student: Student):
        return self.all_students.append(student)
    
    def get_students(self):
        return self.all_students

class AverageScore:
    def get_average_score(self, students_list: list[Student]):
        count = 0
        for s in students_list:
            count += s.score
        
        return count / len(students_list)

class BestStudent:
    def get_best_student(self, students_list: list[Student]):
        best_student_score = 0
        best_student = None
        for s in students_list:
            if s.score > best_student_score:
                best_student = s
                best_student_score = s.score
        return best_student

class Report:
    def print_report(self, best_student, average_score):
        print(f'Average score: {average_score}')
        print(f'Best student: {best_student}')
    
    
students = StudentsList()
students.add_student(Student('Andrew', 11.1))
students.add_student(Student('Mike', 10.0))
students.add_student(Student('Mitya', 12.0))

best = BestStudent().get_best_student(students.all_students)
avg = AverageScore().get_average_score(students.all_students)

print(students.get_students())
print(avg)
print(best)
print(Report().print_report(best, avg))