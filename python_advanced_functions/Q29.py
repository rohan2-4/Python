# Create two decorators:
# - uppercase: converts the returned string into uppercase.
# - add_stars: adds *** before and after the returned string.
from functools import wraps
def uppercase(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result= func(*args,**kwargs)
        return result.upper()
    return wrapper

def add_stars(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result= func(*args,**kwargs)
        return f"***{result}***"
    return wrapper
@uppercase
@add_stars
def message():
    return "welcome to python development"
print(message())  