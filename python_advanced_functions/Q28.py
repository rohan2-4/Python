# Create a decorator called execution_info.

# It should:
# 1. Print "Function is starting...".
# 2. Execute the original function.
# 3. Print "Function is completed!".
# 4. Support positional and keyword arguments.
# 5. Return the original function's result.
def execution_info(func):
    def wrapper(*args,**kwargs):
        print("Function is starting..... ")
        result=func(*args,**kwargs)
        print("Function is completed ! ")
        return result
    return wrapper
@execution_info
def calculate_sum(a, b):
    return a + b
new =calculate_sum(20,45)
print(f"Sum is {new} ")
        