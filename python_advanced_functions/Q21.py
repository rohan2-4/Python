# Write a recursive function to calculate the sum of digits.
def sum_digits(n):
    if n<10:
        return n
    return (n%10) + sum_digits(n//10)
print(sum_digits(1257890))
