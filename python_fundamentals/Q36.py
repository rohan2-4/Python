#. Write a Python function that accepts an employee dictionary and returns the name of the employee with the highest salary.
def get_highest_paid_employee(employees):
    if not employees:
        return None
    highest_paid = max(employees.values(), key=lambda emp: emp["Salary"])
    return highest_paid["Name"]


# Example usage
employee_records = {
    "emp_1": {"Name": "Aarav Sharma", "Role": "Software Engineer", "Salary": 650000},
    "emp_2": {"Name": "Priya Patel", "Role": "Data Analyst", "Salary": 600000},
    "emp_3": {"Name": "Rohan Deshmukh", "Role": "Backend Developer", "Salary": 850000},
}

top_earner = get_highest_paid_employee(employee_records)
print(f"Highest Paid Employee: {top_earner}")
