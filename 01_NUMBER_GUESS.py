"""
Number Guessing Game
Author: Aniket M. Warghat
Description: A simple CLI game where the user guesses a random number 
between 1-100 within a limited number of attempts.
"""

import random as rm

# Initialize game constants and variables
number = rm.randint(1, 100)      # The target number to guess
active = True                    # Flag to control the game loop
counter = 0                      # Tracks the number of guesses made
number_attempts = 15             # Maximum allowed attempts

while active and counter < number_attempts:
    try:
        # Prompt user and increment the attempt counter
        guess = int(input("Enter Value Between 1-100: "))
        counter += 1
        
        # Check if the guess is too high
        if guess > number:
            attempt = number_attempts - counter
            print(f"Guess lower, attempts left: {attempt}")
            
        # Check if the guess is too low
        elif guess < number:
            attempt = number_attempts - counter
            print(f"Guess higher, attempts left: {attempt}")
            
        # Success condition: Guess matches the random number
        elif guess == number:
            print(f"Correct Guess! Congratulations! The number was {number}. "
                  f"You guessed it in {counter} attempts.")
            active = False # Break the loop

    except ValueError:
        # Handles non-integer inputs to prevent the script from crashing
        print("Invalid input! Please enter a whole number.")

# Final check: If the loop ended because attempts ran out
if counter == number_attempts and guess != number:
    active = False
    print(f"Game Over! The number was {number}. "
          f"You are out of attempts ({counter}/{number_attempts}).")