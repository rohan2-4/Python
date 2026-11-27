# filter(): Extract names with more than five characters.
names = ["Rohan", "Amit", "Priya", "Alexander", "Rahul"]
result = list(filter(lambda name : len(name) > 5,names))
print(result)