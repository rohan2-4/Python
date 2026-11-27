#  Write a function called product_details() that accepts any number of keyword arguments and returns only the details where the key is "price", "brand", or "category".
def product_details(**kwargs):
    allowed = {'price','brand','category'}
    return{key:value for key,value in kwargs.items() if key in allowed}

p1=product_details(
    name="Laptop",
    price=55000,
    brand="HP",
    category="Electronics",
    color="Silver"
)
print(p1)
