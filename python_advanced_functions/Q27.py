# Create a decorator called calculate_time.

# Requirements:
# 1. Record the start time using time.time().
# 2. Execute the original function.
# 3. Record the end time.
# 4. Calculate execution time.
# 5. Print execution time in seconds.
# 6. Return the original function's result.
from functools import wraps
import time 
def calculate_time(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        starting_time = time.time()
        result = func(*args,**kwargs)
        ending_time = time.time()
        execution_time = ending_time - starting_time
        print(f"{func.__name__} excuted in {execution_time:.6f} seconds ")
        return result
    return wrapper
@calculate_time
def process_data():
    time.sleep(2)
    return "Data processing completed"
result =process_data()
print(result)
