class Note:
    title: str
    description: str
    
    def __init__(self, title: str, description: str = ''):
        self.title = title
        self.description = description

note = Note('note1', 'make lesson')

print(note.description)