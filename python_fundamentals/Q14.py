# Remove duplicate elements from a list while preserving the original order . 
list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
new_list = []
for num in list1:
    if num not in new_list:
        new_list.append(num)
print("The list after removing duplicates:  ",new_list)
