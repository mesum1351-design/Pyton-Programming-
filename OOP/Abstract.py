from abc import ABC, abstractmethod

# 1. Abstract Base Class (The Mandatory Rule/Blueprint)
class Payment(ABC):
  @abstractmethod
  def make_payment(self, amount):
    pass  # No code here! Child classes MUST write their own version.
# 2. Child Class 1: Credit Card
class CreditCardPayment(Payment):
  def make_payment(self, amount):
    print(f"Paid ${amount} securely using Credit Card.")
# 3. Child Class 2: PayPal
class PayPalPayment(Payment):
  def make_payment(self, amount):
    print(f"Paid ${amount} securely using PayPal account.")

# If you try to use the abstract class directly, Python stops you:
# p = Payment()  # Error! Cannot instantiate abstract class

# Using the child classes:
cc = CreditCardPayment()
cc.make_payment(150)  # Output: Paid $150 securely using Credit Card.

pp = PayPalPayment()
pp.make_payment(45)  # Output: Paid $45 securely using PayPal account.