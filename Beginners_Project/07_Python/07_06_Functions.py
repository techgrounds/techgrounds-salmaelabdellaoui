# Exercise 1
import random

# Print 5 random integers between 0 and 100
for _ in range(5):
    random_integer = random.randint(0, 100)
    print(random_integer)

# Exercise 2
# Define a custom function myfunction() that prints "Hello, world!"
def myfunction():
    print("Hello, world!")

# Call myfunction
myfunction()

# Define a modified function myfunction_with_name() that takes a string argument
def myfunction_with_name(name):
    print(f"Hello, {name}!")

# Call myfunction_with_name with a specific name
myfunction_with_name("Salma El Abdellaoui")

# Exercise 3
def avg(a, b):
    # Calculate and return the average of the given parameters a and b
    return (a + b) / 2
    
# you are not allowed to edit any code below here
x = 128
y = 255
z = avg(x, y)

print("The average of",x,"and",y,"is",z)
