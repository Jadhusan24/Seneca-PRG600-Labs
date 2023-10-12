#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Lab 2 Challenge 3
Author - JD
'''

def decimal_to_binary(decimal_number):
    binary_result = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_result = str(remainder) + binary_result
        decimal_number = decimal_number // 2

    if not binary_result:
        binary_result = "0"

    return binary_result

def main():
    try:
        decimal_number = int(input("Enter a decimal number: "))

        if decimal_number < 0:
            print("Please enter a non-negative decimal number.")
        else:
            binary_result = decimal_to_binary(decimal_number)
            print(f"The binary representation of {decimal_number} is: {binary_result}")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

    except KeyboardInterrupt:
        print("\nConversion interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
