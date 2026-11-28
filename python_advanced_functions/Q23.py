# Create a function greeting(message) that returns an inner function. The inner function accepts a person's name and prints the greeting.
def greeting(message):
    def inner_function(name):
        print(f"{message},{name}!")
    return inner_function
say_hello = greeting("Good Morning")
say_hello("Rohan")
