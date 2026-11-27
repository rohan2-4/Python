# Sort the following employees by salary, from highest to lowest.
employees = [
    {"name": "Rohan", "salary": 30000},
    {"name": "Amit", "salary": 45000},
    {"name": "Rahul", "salary": 25000},
    {"name": "Sneha", "salary": 55000}
]
result = sorted(employees, key= lambda x: x['salary'],reverse= True)
for x  in result:
    print(x['name'],x['salary'])