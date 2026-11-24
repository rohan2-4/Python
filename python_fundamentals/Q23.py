# Use extended unpacking to get:
# - First element
# - Middle elements
# - Last two elements
# Do not use indexing to extract each individual element
numbers = (10, 20, 30, 40, 50, 60, 70)
first,*middle,secondlast,last=numbers
print(first)
print(middle)
print(secondlast,last)