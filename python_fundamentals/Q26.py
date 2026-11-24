# Find union, intersection, A-B and symmetric difference.
A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
# there are two ways to find union
print(A|B)
print(A.union(B))
#There are two ways to find intersection
print(A&B)
print(A.intersection(B))
# there are two ways to find the difference
print(A-B)
print(A.difference(B))
# symetric diffrence
print(A.symmetric_difference(B))