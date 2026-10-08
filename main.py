from functools import wraps

# My version ->
# def limit_calls(times):
#     def decorator(fn):
#         def wrapper(*args):
#             counter_name = f"{fn.__name__}_counter"
#             slf = args[0]
#             if not hasattr(slf.__class__, counter_name):
#                 setattr(slf.__class__, counter_name, 1)
#             else:
#                 setattr(slf.__class__, counter_name, getattr(slf.__class__, counter_name) + 1)
                
#             if getattr(slf.__class__, counter_name) > times:
#                 raise ValueError('Engine should rest!')
#             return fn(*args)
#         return wrapper
#     return decorator

# def limit_calls(max_calls: int):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(self, *args, **kwargs):
#             count_attr = f"_{fn.__name__}_count"
#             current = getattr(self, count_attr, 0)
#             if current >= max_calls:
#                 raise RuntimeError('Call limit exceeded')
#             setattr(self, count_attr, current + 1)
#             print(f"[LOG] {fn.__qualname__} called {current + 1} / {max_calls}")
#             return fn(self, *args, **kwargs)
#         return wrapper
#     return decorator

class Limit:
    def __init__(self, count: int):
        self.count = count
        
    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if self.count <= 0:
                raise RuntimeError('Call limit exceeded')
            self.count -= 1
            return fn(*args, **kwargs)
        return wrapper

class Engine:
    @Limit(3)
    def start(self):
        print('engine is started')

car = Engine()

car.start()
car.start()
car.start()
car.start()