#!/usr/bin/python3
'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Main Lab 2 - lab3b 
Author - JD
'''

def main():
    x = 0 

    try:
        while x <= 10:
            print(x)  
            x += 1    #incrementing x by 1
        print("Finished")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
