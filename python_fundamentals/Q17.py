# Rotate a list to the right by k positions.
list1 = [1,2,4,5,6,7,9]
k= 10
if list1:
    k= k % len(list1)
    rotated =list1[-k:]+list1[:-k]
else:
    rotated=[]
print(rotated)