def log(func):
    """Logger function"""
    def wrapper(*args, **kwargs):
        print(f"Invoke {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@log
def add(a: float, b: float) -> float:
    return a + b

print(add(4, 4))