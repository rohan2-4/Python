# Print all employee names.
# Find employees whose salary is above ₹35,000.
# Calculate the average salary.
# Find the employee with the highest salary.
# Increase every employee's salary by 10%.
# Create a new dictionary containing only employees whose updated salary is above ₹40,000.
employees = {
    101: {"name": "Rohan", "salary": 30000},
    102: {"name": "Amit", "salary": 45000},
    103: {"name": "Sneha", "salary": 35000},
    104: {"name": "Rahul", "salary": 50000},
    105: {"name": "Priya", "salary": 25000}
}
# Print all employee names.
for key,value in employees.items():
    print(key,":",value['name'])
# Find employees whose salary is above ₹35,000.
for jobid,details in employees.items():
    if details['salary'] > 35000:
        print(f"{details['name']} - {details['salary']}")
# Calculate the average salary.
total = sum(details['salary'] for details in employees.values())
avg_salary = total / len(employees)
print(avg_salary)
# Find the employee with the highest salary.

highest_paid = max(employees.values(), key=lambda job: job['salary'])
print("highest ",highest_paid)
# Increase every employee's salary by 10%.
for value in employees.values():
    value['salary']=round(value['salary'] * 1.10)
for key,value in employees.items():
    print(key,":",value)
# Create a new dictionary containing only employees whose updated salary is above ₹40,000.
print("high gainers")
High_earners ={
    key:value
    for key,value in employees.items()
    if value['salary'] > 40000
}
for key,value in High_earners.items():
    print(key,":",value)