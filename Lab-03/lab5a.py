#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 3 - lab5a 
Author - JD
'''

def my_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

if __name__ == "__main__":
    user_numbers = []
    print("Calc")
    
    try:
        while True:
            user_input = input("Type a number to add to your sum. -- Enter will exit. ")
            
            if user_input == "":
                break
            else:
                user_numbers.append(int(user_input))
        
        if not user_numbers:
            print("No numbers. Cannot calculate the average :(")
        else:
            num_sum = my_sum(user_numbers)
            num_length = len(user_numbers)
            average = num_sum / num_length
            print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this is: {average}.")
    
    except KeyboardInterrupt:
        print("\nHave a nice day :).")
    
    print("Thank you for using the calc.")
