#1. NUMBER GUESSING GAME

import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif user_guess < number_to_guess:
                print("Your guess is too low. Try again!")
            else:
                print("Your guess is too high. Try again!")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
