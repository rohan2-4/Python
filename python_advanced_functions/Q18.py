# Create an outer function with a variable count = 0. Inside it, create an inner function that increments count using nonlocal.
# Call the inner function three times.
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(f"the function called {count} times ")
    inner()
    inner()
    inner()
outer()