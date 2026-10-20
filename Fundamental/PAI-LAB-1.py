
A = {1.3, 23.21, 3.3}
B = {7.17, 43.4, 9.91, 87.73}
print(A.union(B))
print(len(A))
print(len(B))
A.remove(3.3)
print(A)

#Write a program that takes a list of numbers.
#(For example, a = [5, 10, 15, 20, 25] and makes a new list of
#only the first and last elements of the given list. For practice, you can
#write this code using lambda function.

a = [1,2,3,4,5,6]
FL = lambda lst: [lst[0], lst[-1]] if lst else []
result = FL(a)
print(result)

#Write a program (function!) that takes a list and returns a new list that contains all the elements
#of the first list minus all the duplicates.
def remove_duplicate(lst):
    return list(set(lst))
a = [1,2,3,3,4,5,4]
print(remove_duplicate(a))

#Create a program that asks the user for a number and then prints out a list of all the divisors of
#that number. (If you don’t know what a divisor is, it is a number that divides evenly into
#another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Enter a number: "))
print ("Divisor of number of ",num )
divisor = [i for i in range(1,num +1) if num % i == 0]
print (divisor)


#Write a program that returns a list that contains only the elements that are common
#between the lists (without duplicates). Make sure your program works on two lists of
#different sizes. Use list comprehensions.
a = [1,2,3,4,5,6]
b = [2,3,4,5,7]
common = [i for i in a if i in b]
print (common)

