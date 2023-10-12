#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab4a 
Author - JD
'''

from random import randint

def main():
    try:
        secret = randint(1, 10)
        user_guess = 0

        print("---------------Guess a number between 1 and 10:---------------")

        while user_guess != secret:
            user_input = input("Enter a number: ")

            try:
                user_guess = int(user_input)
            except ValueError:
                print("Error: not a number or out of bounds.")
                continue

            if user_guess < 1 or user_guess > 10:
                print("Error: not a number or out of bounds.")
            elif user_guess == secret:
                print("Correct! You win.")
            elif user_guess < secret:
                print("Sorry, try again. Guess a higher number:")
            elif user_guess > secret:
                print("Sorry, try again. Guess a lower number:")

    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

if __name__ == "__main__":
    main()
