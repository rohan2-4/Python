# Create a decorator called validate_input.

# Requirements:
# 1. Accept positional and keyword arguments.
# 2. Check whether all supplied arguments are positive numbers.
# 3. If any argument is negative or not numeric, print "Invalid input" and return None.
# 4. Otherwise, execute the original function and return its result.
from functools import wraps

def validate_input(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        all_values = args + tuple(kwargs.values())

        if not all(
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and value > 0
            for value in all_values
        ):
            print("Invalid input")
            return None

        result = func(*args, **kwargs)
        return result

    return wrapper


@validate_input
def calculate_product(a, b):
    return a * b


print(calculate_product(10, 20))
print(calculate_product(10, -5))
print(calculate_product(10, b=5))
print(calculate_product(10, "hello"))