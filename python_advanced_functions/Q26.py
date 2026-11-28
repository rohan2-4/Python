# Create a decorator called start_end that prints
# Program Started
# Welcome to Python Development!
# Program Finished
def start_end(func):
    def wrapper():
        print("Program Started ")
        func()
        print("Program Finished")
    return wrapper
def message():
    print("Welcome To Python Development")
message = start_end(message)
message()