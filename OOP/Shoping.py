
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return
        print(name, "not found.")
    def update_quantity(self, name, quantity):
        for product in self.products:
            if product["name"] == name:
                product["quantity"] = quantity
                print("Quantity updated.")
                return
        print(name, "not found.")
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product["price"] * product["quantity"]
        return total
    def display_bill(self):
        print("\nCustomer:", self.customer_name)
        print("----- Shopping Bill -----")
        for product in self.products:
            amount = product["price"] * product["quantity"]
            print(product["name"], "| Price:", product["price"],
                  "| Quantity:", product["quantity"],
                  "| Amount:", amount)

        print("Total Bill:", self.calculate_total())
        print("-------------------------")


# Creating 2 shopping cart objects
cart1 = ShoppingCart("Mesum")
cart2 = ShoppingCart("Ahmed")

# Adding products to cart 1
cart1.add_product("Laptop", 80000, 1)
cart1.add_product("Mouse", 1500, 2)

# Testing operations on cart 1
cart1.update_quantity("Mouse", 3)
cart1.display_bill()

# Adding products to cart 2
cart2.add_product("Keyboard", 2500, 1)
cart2.add_product("Headphones", 3000, 2)

# Testing operations on cart 2
cart2.remove_product("Keyboard")
cart2.display_bill()