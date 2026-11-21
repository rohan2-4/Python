# Remove duplicate characters from a string while preserving order.
text = input("Enter the string: ")
result = ""
for char in text:
    if char not in result:
        result += char
print("The string after removing duplicate characters is: ", result)