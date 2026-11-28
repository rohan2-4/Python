# Create a closure-based bank account that:
# - Starts with a given balance.
# - Has an inner deposit function.
# - Has an inner withdraw function.
# - Has an inner check-balance function.
def create_account(initial_balance=0):
    balance = initial_balance
    def deposit(amount):
        nonlocal balance
        if amount <0: 
            return "Deposit amount must positive  " 
        balance+=amount
        return f"The {amount} rs depoisted in account"
    def withdraw(amount):
        nonlocal balance
        if amount < 0:
            return "Withdrwal amount must be positive"
        if amount > balance:
            return "Insufficient funds"
        balance-=amount
        return f"The {amount} rs is withdrawn from your account"
    def check_balance():
        return balance
    return{
        "deposit":deposit,
        "withdraw":withdraw,
        "check_balance":check_balance,
    }
account=create_account(10)
print(account["check_balance"]())
print(account["deposit"](50))
print(account["withdraw"](30))
print(account["check_balance"]())

