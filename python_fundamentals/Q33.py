# Create a dictionary containing three employees, each with:
# - Employee ID
# - Name
# - Department
# - Salary
# Print the name of the second employee and update the salary of the first employee.
company={
    101:{
        'name' :'Rohan',
        'department':'developer',
        'salary':30000 
    },
    102:{
        'name':'Krushna',
        'department':'HR',
        'salary':35000
    },
    103:{
        'name':'Kaustubh',
        'department':'developer',
        'salary': 27000

    }
}
print(company)
print(company[102]["name"])
company[101]["salary"]=40000
print(company[101])