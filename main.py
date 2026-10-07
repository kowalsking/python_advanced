from functools import wraps

def log_call(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {fn.__qualname__} args={args}")
        return fn(*args, **kwargs)
    return wrapper

class Service:
    @log_call
    def process(self, x: float) -> float:
        return x * 2
    
s = Service()
s.process(4)

def a():
    return 1

print(a.__name__)
print(s.process.__name__)