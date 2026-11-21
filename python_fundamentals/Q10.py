#Find the first non-repeating character in a string.
text= input("Enter the string: ")
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

for char in text:
    if freq[char] == 1:
        print("The first non-repeating character is: ", char)
        break
else:
    print("There is no non-repeating character in the given string.")