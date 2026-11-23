#Flatten a two-dimensional list into a one-dimensional list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list= [x for sub in matrix for x in sub]
print(flat_list)