#Count the number of vowels in a given string.
text = input("Enter the text:  ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count +=1
    else:
        continue
print("The number of vowels in the given string is: ",count)