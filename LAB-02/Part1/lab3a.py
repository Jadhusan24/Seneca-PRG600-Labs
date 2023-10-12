#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab3a 
Author - JD
'''

def main():
    questions = [
        ("Enter the answer to 12 + 14, or press 's' to skip: ", 26),
        ("Enter the answer to 23 + 8, or press 's' to skip: ", 31),
        ("Enter the answer to 30 + 13, or press 's' to skip: ", 43),
        ("Enter the answer to 17 + 27, or press 's' to skip: ", 44)
    ]

    score = 0
    total_questions = len(questions)
    try:
        for question, answer in questions:
            num = 0
            while num != answer:
                user_input = input(question)
                if user_input.lower() == 's'or user_input.upper() == 'S': #added capital S for skip!
                    print("Question skipped. 0 points awarded.")
                    break
                else:
                    num = int(user_input)
                    if num != answer:
                        print("Incorrect. Try again.")
                    else:
                        score += 1
                        print("Correct! You have been awarded 1 point!")

            print("Next question...")

        percentage = (score / total_questions) * 100
        print(f"You received a grade of {percentage:.1f}%.")
        
    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

if __name__ == "__main__":
    main()
