#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 3 - lab5d 
Author - JD
'''

import sys

print(f"Arguments: {sys.argv}")
print(f"The name of the file you are running is: {sys.argv[0]}.")

if len(sys.argv) == 1:
    print("No arguments found.")
else:
    for arg in sys.argv[1:]:
        print(f"Argument found: {arg}.")

print("Complete.")
