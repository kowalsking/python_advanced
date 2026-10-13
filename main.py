from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    score: float

@dataclass
class StudentRepository:
    students: list[Student] = field(default_factory=list)

    def add(self, student: Student):
        return self.students.append(student)
    
    def list_all(self) -> list[Student]:
        return self.students

@dataclass
class StatisticService:
    repository: StudentRepository
    
    def get_average_score(self) -> float:
        students = self.repository.list_all()
        if not students:
            return 0
        total = sum(s.score for s in students)
        return total / len(students)

    def get_best_student(self) -> Student:
        students = self.repository.list_all()
        return max(students, key=lambda s: s.score)
    

@dataclass
class ReportPrinter:
    repository: StudentRepository
    stat_service: StatisticService

    def print_report(self):
        print('Students report')
        for s in self.repository.list_all():
            print(f'{s.name}: {s.score}')
        print(f'Average score: {self.stat_service.get_average_score()}')
        print(f'Best student: {self.stat_service.get_best_student().name}')
    
    
repo = StudentRepository()
repo.add(Student('Andrew', 11.1))
repo.add(Student('Mike', 10.0))
repo.add(Student('Mitya', 12.0))

stat_service = StatisticService(repo)
printer = ReportPrinter(repo, stat_service)

printer.print_report()