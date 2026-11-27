# Write a recursive factorial function that handles negative input.
def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print(factorial(4))