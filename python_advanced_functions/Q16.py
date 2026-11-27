# Write a function that counts how many times it has been called, using a variable outside the function.
x= 0
def Track_calls():
    global x
    x+=1
    print(f"function has beenn called  {x} times ")
Track_calls()
Track_calls()
Track_calls()