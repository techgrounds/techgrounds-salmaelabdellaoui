# Exercise 1
# Use the input() function to ask the user for their name
user_name = input ("Enter your name: ")

# Check if the entered name is your name
your_name = "Salma El Abdellaoui"  # Replace this with your actual name

if user_name == your_name:
    # Print a personalized welcome message if the name matches
    print(f"Welkom, {user_name}!")
else:
    # Print a different personalized message if the name doesn't match
    print(f"Zou jij van mij pagina af willen, {user_name}!")


# Exercise 2 
while True:
    # Ask the user for a number
    user_input = input("Enter a number (type 'exit' to end the game): ")

    # Check if the user wants to exit the game
    if user_input.lower() == 'exit':
        print("Exiting the game. Goodbye!")
        break

    # Convert the user input to a number
    try:
        user_number = float(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Provide a response based on the user's number
    if user_number > 100:
        print("Je gaat veel te hoog, blijf doorgaan 100.")
    elif user_number < 100:
        print("Dit is lager dan 100 probeer het nog een keer.")
    else:
        print("Congratulations! You entered 100. The game is over.")
        break
    

