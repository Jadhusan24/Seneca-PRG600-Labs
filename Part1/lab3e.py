#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab3e 
Author - JD
'''

import random

def main():
    score = 0
    total_questions = 0
    skipped_questions = 0

    try:
        while True:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            answer = num1 + num2

            user_input = input(f"Enter the answer to {num1} + {num2}, press 's' to skip or 'q' to quit: ")

            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 's':
                skipped_questions += 1
                print("Question skipped. 0 points awarded.")
            else:
                try:
                    user_answer = int(user_input)
                    if user_answer == answer:
                        score += 1
                        print("Correct! You have been awarded 1 point!")
                    else:
                        print("Incorrect. Try again.")
                except ValueError:
                    print("Error: Not a number or out of bounds.")

            total_questions += 1

    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

    percentage = (score / total_questions) * 100 if total_questions > 0 else 0

    print(f"Quiz over. You scored {percentage:.1f}%.")

if __name__ == "__main__":
    main()
