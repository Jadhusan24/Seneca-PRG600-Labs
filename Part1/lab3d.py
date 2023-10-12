#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab3d 
Author - JD
'''

from random import randint  # Import the randint function from the random module

def main():
    try:
        secret = randint(1, 10)  # Generate a random secret number between 1 and 10
        user_guess = 0

        print("Guess a number between 1 and 10:")

        while user_guess != secret:
            user_input = input()

            try:
                user_guess = int(user_input)
            except ValueError:
                print("Please enter a valid number between 1 and 10.")
                continue

            if user_guess == secret:
                print("Correct! You win.")
            elif user_guess < 1 or user_guess > 10:
                print("Please enter a number between 1 and 10.")
            elif user_guess < secret:
                print("Sorry, that's not it. Guess a higher number:")
            elif user_guess > secret:
                print("Sorry, that's not it. Guess a lower number:")

    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

if __name__ == "__main__":
    main()
