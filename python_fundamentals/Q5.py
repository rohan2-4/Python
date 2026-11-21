# Write a program to calculate the factorial of a number.
num = int(input("Enter the number of factorial: " ))
fact =1 
for i in range(1,num+1):
    fact *=i
    
print(fact)