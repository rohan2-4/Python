# Find the second-largest distinct element in a list without using sorted() or max()
new_list = [10,10,20,40,50]
 
for num in new_list:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num 

print("The second largest distinct element is:", second)