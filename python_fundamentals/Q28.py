# Find:
# - Developers who know both languages.
# - Developers who know only Python.
# - Developers who know only Java.
# - All unique developers.
python_developers = {"Rohan", "Amit", "Rahul", "Sneha"}
java_developers = {"Amit", "Sneha", "Priya", "Karan"}
a = python_developers.intersection(java_developers)
print("The developers who knows the both languages",a)
b= python_developers-java_developers
print("the developers who knows only python",b)
c= java_developers-python_developers
print("the developers who knows only Java",c)
d= python_developers.union(java_developers)
print("All unique developer",d)


# Write a Python program to find the common elements between two lists without using loops or list comprehensions.
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
s1=set(list1)
s2=set(list2)
print(s1.intersection(s2))