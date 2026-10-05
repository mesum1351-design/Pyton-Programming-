# Random Module print integer number in range
import random
num1 = random.randint(1,100)
print(num1)

#Print Random Decimal Number
num2 = random.random()
print(num2)

#Task: Generate a random positive integer less than 10.
import random
random.randint(1,10)

#Task: Generate a random integer within 0 (inclusive) and 100 (inclusive)
import random
random.randint(0,100)

#Task: Generate a random integer within a and b, where a and b are user entered integers and a  <=  b
import random
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if(a<=b):
 num = random.randint(a,b)
 print(num)

 #Task: Generate a random float number between 0 and 1
 import random

 random.random()

 #Task: Generate a random float number between 0 and 10.
 import random

 random.uniform(0, 100)

 #Task: Generate a random float number between 5 and 10
 import random

 random.uniform(5, 10)

 #Task: Generate a random float number based on the Gaussian distribution
 import random

 random.gauss(0, 10)

 #Random Datasets
#Genearte a list of 1000 random floats within 0 and 1.

import random
num = [random.uniform(0,1) for i in range(1000)]
print(num)

#Generate a list of 1000 random integers within 0 and 1.
import random
rand = [random.randint(0,1) for i in range(1000)]
print(rand)

#Generate a list of 1000 numbers following normal distribution with 10 as mean, and 1 as standard derivation.
import random

numbers = [random.normalvariate(10, 1) for i in range(1000)]

print(numbers)
