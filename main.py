class Task:
    done: bool = False
    title: str
    
    def set_info(self, text: str):
        self.title = text
    
    def get_info(self):
        return self.title

        
task = Task()
task.set_info('make python lesson')
print(task.get_info())