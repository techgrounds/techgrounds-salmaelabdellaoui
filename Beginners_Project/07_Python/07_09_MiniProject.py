# Number Guessing

import random

def generate_random_number():
    return random.randint(1, 100)  # You can adjust the range as needed

def provide_clue(secret_number, guess):
    if guess < secret_number:
        return "Too low! Try a higher number."
    elif guess > secret_number:
        return "Too high! Try a lower number."
    else:
        return ""

def play_game():
    secret_number = generate_random_number()
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the specified range.")
                continue

            clue = provide_clue(secret_number, guess)
            print(clue)

            if guess == secret_number:
                print(f"Gefeliciteerd! Je hebt de juiste nummer geraden in {attempts} mogelijkheden.")
                break

        except ValueError:
            print("Niet geldig. Probeer het opnieuw.")

if __name__ == "__main__":
    play_game()
