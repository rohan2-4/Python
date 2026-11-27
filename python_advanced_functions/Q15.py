# Given employee records:
# - Increase each employee's salary by 15%.
# - Select employees whose updated salary exceeds ₹40,000.
# - Print their names and updated salaries.
employees = [
    {"name": "Rohan", "salary": 30000},
    {"name": "Amit", "salary": 45000},
    {"name": "Sneha", "salary": 55000},
    {"name": "Rahul", "salary": 25000}
]
updated=list(map(lambda emp:{**emp ,'salary':emp['salary']*1.15},employees))
print(updated)
high_gainers= list(filter(lambda emp : emp['salary'] > 40000,updated))
print(high_gainers)