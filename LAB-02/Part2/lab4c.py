#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab4c 
Author - JD
'''

import math

def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def main():
    print("Circle Area Calculator")
    try:
        while True:
            user_input = input("Enter a radius between 0 and 1999. Press Enter to exit: ")

            if user_input == "":
                print("Exiting...")
                break

            try:
                radius = int(user_input)
                if 0 <= radius <= 1999:
                    area = circle_area(radius)
                    print(f"Radius: {radius}. Area: {area}.")
                else:
                    print(f"Error: {radius} is out of range.")
            except ValueError:
                print(f"Error: {user_input} is not a number.")
    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

if __name__ == "__main__":
    main()
