# def retry(times: int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 try:
#                     func(*args, **kwargs)
#                 except ValueError as e:
#                     pass
#         return wrapper
#     return decorator


def retry(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attemp in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Try {attemp} don'c completed: {e}")
                    if attemp == times:
                        print('All attemps compleated')
        return wrapper
    return decorator


import random

@retry(3)
def unstable():
    if random.random() < 0.7:
        raise ValueError('Network error')
    print('Success!')
    
unstable()