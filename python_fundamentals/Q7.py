#Check whether a string is a palindrome.
text = input("Enter the word:  ")
reverse = text[::-1]
if text == reverse:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")