class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be Negative...")
        else:
            print("Setting price...")
            self._price = value
    @price.deleter
    def price(self):
        print("Deleting Price...")
        del self._price

# Create a Product object
p = Product(100)

# Access the price (getter)
print(p.price)

# Update the price (setter)
p.price = 150
print(p.price)

# Try setting a negative price (setter validation)
p.price = -20

# Delete the price (deleter)
del p.price




