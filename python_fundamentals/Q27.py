# Remove duplicates and preserve the original order.
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
new= list(dict.fromkeys(numbers))
print(new)