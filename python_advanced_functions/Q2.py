# Write a function that accepts multiple numbers and returns the largest number. Handle the case where no numbers are passed.
def largest_number(*args):
    if not args:
        return None
    return max(args)
result = largest_number(10,20,40,50,70)
print(result)
n= largest_number()
print(n)