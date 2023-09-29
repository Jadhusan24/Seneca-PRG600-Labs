'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Challenge 2 program
'''

decimal_number = input("Enter a decimal number (eg: 5.8) : ") #getting user input.

try: #using exception handling
    rounded_integer = int(float(decimal_number) + 0.5) #take the user input convert it to float and adding 0.5 to round the value
    print(f"The rounded number for {decimal_number} is {rounded_integer}") #prints the rounded value now
except ValueError: 
    print("Enter only valid decimal number") #exception