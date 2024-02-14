def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator function called")
        return func(*args, **kwargs)
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()