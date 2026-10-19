class Vehicle:
  def max_speed(self):
    print("Vehicle max speed is 150")
# Child Class (Inherits from Vehicle)
class Car(Vehicle):
  # Method Overriding: same name, different behavior for a car
  def max_speed(self):
    print("Car max speed is 240")
# Usage
v = Vehicle()
v.max_speed()  # Output: Vehicle max speed is 150

c = Car()
c.max_speed()  # Output: Car max speed is 240