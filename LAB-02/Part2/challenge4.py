#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Lab 2 Challenge 4
Author - JD
'''

def rtrn_slope(x1, y1, x2, y2):
    """Calculate the slope between two points (x1, y1) and (x2, y2)."""
    return (y2 - y1) / (x2 - x1)

def main():
    print("Please note: X and Y values must be between 0 and 10.")

    prev_x = float(input("Enter the starting X value: "))
    prev_y = float(input("Enter the starting Y value: "))

    try:
        while True:
            new_x = float(input("Enter the new X value: "))
            new_y = float(input("Enter the new Y value: "))

            if 0 <= prev_x <= 10 and 0 <= prev_y <= 10 and 0 <= new_x <= 10 and 0 <= new_y <= 10:
                slope = rtrn_slope(prev_x, prev_y, new_x, new_y)
                print(f"Slope is: {slope}")
            else:
                print("Error: X and Y values must be between 0 and 10.")

            option = input("Press Enter to continue or 'q' to quit: ")
            if option.lower() == 'q':
                break

            prev_x, prev_y = new_x, new_y
    except KeyboardInterrupt:   #added ctrl + c Exception
        print("\n Until Next Time")

if __name__ == "__main__":
    main()
