# Create a global variable balance = 5000. Write a function deposit() that adds ₹1000 to it each time.
balance = 5000
def deposit():
    global balance
    balance+=1000
    print(f"The available balance is  {balance}rs ")
deposit()
deposit()
