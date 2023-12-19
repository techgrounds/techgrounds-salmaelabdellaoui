# Exercise 1

a = 'int'
b = 7
c = False
d = "18.5"

# Determine and print the data types of variables a, b, c, and d
print("Data type of 'a':", type(a))
print("Data type of 'b':", type(b))
print("Data type of 'c':", type(c))
print("Data type of 'd':", type(d)) 

# Make a new variable 'x' and give it the value of b + d
# This will initially result in a TypeError because 'b' is an integer and 'd' is a string
# To fix it, we convert 'd' to a float before performing the addition
x = b + float (d) 

# Print the value of x, which should now be a float
print("Value of x:", x) 