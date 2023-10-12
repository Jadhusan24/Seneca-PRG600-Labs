#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab3c 
Author - JD
'''

def main():
    sum = 0
    print("SUMMING CALCULATOR")
    try:
        while True:
            print("The sum so far: " + str(sum))
            user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
            
            if user_input == "":
                break
            else:
                sum += int(user_input)

        print("Thank you for using summing calculator. The final sum was " + str(sum) + ".")
    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")
        
if __name__ == "__main__":
    main()
