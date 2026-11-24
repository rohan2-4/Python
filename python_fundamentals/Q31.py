#Count the frequency of each number using a dictionary.
numbers = [10, 20, 10, 30, 20, 10, 40, 50, 20]
frequency={}
for num in numbers:
    frequency[num] = frequency.get(num,0) +1 
print(frequency)