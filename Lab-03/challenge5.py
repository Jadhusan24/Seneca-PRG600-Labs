#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 3 - Challenge5 
Author - JD
'''

import random

words = ['pears', 'apple', 'pineapple', 'grape', 'banana', 'orange', 'mangoes', 'strawberry']

secret = random.choice(words)

guessed_letters = []

display_word = ['_'] * len(secret)

def display_current_word():
    print("Your word:")
    print(" ".join(display_word))

print("Welcome Aboard!")

try:
    while True:
        display_current_word()
        
        guess = input("Type your guess: ").lower()
        
        if guess == secret:
            print(f"Congratulations! The word was: {secret}")
            break
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            if guess in secret:
                for i in range(len(secret)):
                    if secret[i] == guess:
                        display_word[i] = guess
                if "_" not in display_word:
                    display_current_word()
                    print("Congratulations!")
                    break
            else:
                print("Sorry, that letter is not in the word.")
        else:
            print("Invalid input. Please enter a single letter or a complete guess.")

except KeyboardInterrupt:
    print("\nHave a nice day :)")
