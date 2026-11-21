# Find the most frequently occurring character in a string.
text= input("Enter the String :  ")
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
max_char = max(freq, key=freq.get)
print("The most frequently occurring character is: ", max_char)