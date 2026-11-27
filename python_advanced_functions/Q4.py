# Create a function using **kwargs that accepts student information and prints every key-value pair.
def student_details(**kwargs):
    print(kwargs)
student_details(
    name="Rohan",
    age=22,
    course="MSc",
    city="Pune"
)