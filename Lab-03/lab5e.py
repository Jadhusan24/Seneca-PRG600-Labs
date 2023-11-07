#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 3 - lab5e
Author - JD
'''

import sys

def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if len(sys.argv) == 1:
    print("Usage: Enter one or more command line arguments.")
    sys.exit(1)

numbers = []
for arg in sys.argv[1:]:
    if is_numeric(arg):
        numbers.append(int(arg))
    else:
        print(f"Error: {arg} is not a number.")

if not numbers:
    print("No valid numbers found.")
else:
    average = calculate_average(numbers)
    print(f"Average for {len(numbers)} numbers: {average:.16f}")


