# Create an employee dictionary.
# - Add a salary.
# - Update the employee's age.
# - Remove the city.
# - Print all keys and values.

emp= {
    "name":"Rohan ",
    "age" : 22,
    "city":"Pune",
    "language":"Python"

}
# - Adding a salary.
emp['Salary'] = 30000
print(emp)
# - Update the employee's age.
emp["age"]=21
print(emp)
# - Remove the city.
emp.pop("city")
print(emp)
# - Print all keys and values.
for key,value in emp.items():
    print(key,":",value)