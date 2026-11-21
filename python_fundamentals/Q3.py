# Write a program to find the largest of three numbers.
a= int(input("Enter the first number :   "))
b= int(input("Enter the second number:   "))
c= int(input("Enter the third number:   "))
if(a==b==c):
    print("All are the equal ",a)
elif(a>=b and a>=c):
    print("the largest number is : ",a)
elif(b>=a and b>=c):
    print("the largest number is : ",b)
else:
    print("largest number is  : ",c)


