def log_call(fn):
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