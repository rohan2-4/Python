# Find the common elements between two lists without duplicates.
list1=[1,2,3,4,6,8,0,6]
list2=[1,2,45,6,7,8,9]
common = list(set(list1) & set(list2))
print(common)