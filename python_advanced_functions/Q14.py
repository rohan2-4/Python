# From the following numbers:
# - First, filter even numbers.
# - Then, calculate their squares.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x %  2 == 0,numbers ))
result = list(map(lambda x : x *x,even ))
print(result)