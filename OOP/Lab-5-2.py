class Product:
    def __init__(self, name, price, quantity, discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
    # Name property
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value
    # Price property
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # Quantity property
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.__quantity = value
    # Discount property
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, value):
        if (not isinstance(value, (int, float))
                or isinstance(value, bool) or not 0 <= value <= 50):
            raise ValueError("Discount must be between 0 and 50")
        self.__discount = value
    # Calculate discounted price of one product
    @property
    def discounted_price(self):
        return self.price * (1 - self.discount / 100)
    # Calculate total price of all products
    @property
    def total_price(self):
        return self.discounted_price * self.quantity


# Creating product object
p1 = Product("Laptop", 100000, 2, 10)

print("Product:", p1.name)
print("Original Price:", p1.price)
print("Quantity:", p1.quantity)
print("Discount:", p1.discount, "%")
print("Discounted Price:", p1.discounted_price)
print("Total Price:", p1.total_price)

# Changing values using setters
p1.price = 120000
p1.quantity = 3
p1.discount = 20

print("\nAfter Changing Values:")
print("Price:", p1.price)
print("Quantity:", p1.quantity)
print("Discount:", p1.discount, "%")
print("Discounted Price:", p1.discounted_price)
print("Total Price:", p1.total_price)
