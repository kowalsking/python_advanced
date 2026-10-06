def log_decorator(func):
    def wrapper():
        print('Function started')
        func()
        print('Function finished')
    return wrapper

@log_decorator
def say_hello():
    print('Hello')

say_hello()
# decorated = log_decorator(say_hello)
# decorated()