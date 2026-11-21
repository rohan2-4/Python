#Count the frequency of each character in a string.
text= input("Enter the string :    ")
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("The frequency of each character in the given string is: ",freq)