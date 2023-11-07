#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 3 - lab5c
Author - JD
'''

import random

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel',
           'vulture', 'horse', 'python', 'capybara']

secret = random.choice(animals)

print("Can you guess what animal is on my mind?")

guessed_letters = set()

try:
    while True:
        guess = input("Enter a letter or a guess. Press Enter to quit: ").lower()

        if guess == "":
            break

        if guess == secret:
            print("You won!")
            break

        if len(guess) == 1 and guess.isalpha():
            if guess in secret:
                print("Yes, my word contains that letter.")
                guessed_letters.add(guess)
            else:
                print("Sorry, my word doesn't contain that letter.")
        else:
            print("Sorry, that's not it. Please enter a single letter or a complete guess.")

except KeyboardInterrupt:
    print("\nHave a nice day :)")

print(f"The secret word was: {secret}")
