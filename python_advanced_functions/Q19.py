# Write a recursive function that prints numbers from 10 down to 1.
def countdown(n):
    if n == 0:
        return ("Done")
    print(n)
    countdown(n-1)
countdown(10)