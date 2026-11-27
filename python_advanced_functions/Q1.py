# Write a function that accepts any number of numbers using *args and returns their sum.
def calculate_sum(*args):
    return sum(args)
result=calculate_sum(1,2,4)
print(result)