# Exercise 1
# Create a variable containing a list of five names
names_list = ["Salma", "Chaima", "Ayoub", "Redouan", "Abdelilah"]

# Loop over the list using a for loop
for name in names_list:
    # Print every individual name on a new line
    print(name)


# Exercise 2 
# Create a list of five integers
integer_list = [10, 20, 30, 40, 50]

# Use a for loop to iterate over the list
for i in range(len(integer_list)):
    # Calculate the sum based on whether it's the last item
    if i == len(integer_list) - 1:
        # If it's the last item, add it to the first item
        sum_value = integer_list[i] + integer_list[0]
    else:
        # Otherwise, add it to the next item in the list
        sum_value = integer_list[i] + integer_list[i + 1]

    # Print the calculated sum
    print(f"Sum of {integer_list[i]} and the next item is: {sum_value}")

