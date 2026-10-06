from datetime import date

class Book:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year
        
    @staticmethod
    def years_since(year: int):
        return date.today().year - year
    
book = Book('Bible', 1934)
print(Book.years_since(book.year))
