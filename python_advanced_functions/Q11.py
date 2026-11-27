# Use filter() and lambda to extract numbers greater than 50.
numbers = [10, 60, 25, 80, 45, 90, 30]
result = list(filter(lambda x :x > 50,numbers))
print(result)