class User:
    age: float
    
u = User()
setattr(u, "age", 10)
print(getattr(u, 'age'))


class Commands:
    def start(self): print('start')
    def stop(self): print('stop')
    def help(self): print('help')
    
cmd = Commands()
action = input('Write command: ')

if hasattr(cmd, action):
    getattr(cmd, action)()
else:
    print("Command don't found!")