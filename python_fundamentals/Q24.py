# Write a function that accepts two numbers and returns:
# - Sum
# - Difference
# - Product
# - Division (handle division by zero)
# Return the results as a tuple.
def calculate(a,b):
    sum = a+b
    difference=a-b
    product=a*b
    if b==0:
        division =0
    else:
        division=a/b
    return (sum,difference,product,division)
new = calculate(27,10)
print(new)