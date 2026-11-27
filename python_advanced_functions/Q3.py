# Write a function that accepts multiple employee salaries and returns:
# - Total salary
# - Average salary
# - Highest salary
# - Lowest salary
def employee(*salaries):
    total_salary = sum(salaries)
    average_salary = total_salary /len(salaries)
    highest_salary = max(salaries)
    lowest_salary= min(salaries)
    return {
 "total":total_salary,
 "average":average_salary,
 "highest_salary":highest_salary,
 "lowest_salary":lowest_salary}
data =employee(10000,20000,30000,500000,6000)
if data is not None:
    for key,value in data.items():
        print(key,":",value)
