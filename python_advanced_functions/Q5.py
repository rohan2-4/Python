# Create a function that accepts any number of keyword arguments and returns an employee dictionary.
def create_employee(**kwargs):
    return kwargs
emp=create_employee(name='Rohan',age=22,city='pune',role='Python developer')
print(emp)