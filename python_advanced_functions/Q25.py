# Create a closure that remembers a multiplier.
def make_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply
times_three=make_multiplier(3)
print(times_three(10))