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

# Excercise 2 

# Use input() to get input from the user and store it in a variable
user_input = input("salmaelabdellaoui")

# Find out the data type of the user input
data_type_of_input = type((user_input))

# Print the user input and its data type
print("User input:", user_input)
print("Data type of input:", user_input)



