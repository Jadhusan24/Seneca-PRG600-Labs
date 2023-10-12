from random import randint

def rtrn_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

rect = rtrn_area(5.5, 3.5)  # Example usage with float values

def print_all_caps(name, age):
    """
    Print a person's name in all caps and their age.

    Parameters:
    name (str): The person's name.
    age (int): The person's age.
    """
    cap_name = name.upper()
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!')

print_all_caps('eric', 41)
print_all_caps('melissa', 40)

def get_rando():
    """
    Generate a random integer between 1 and 100.

    Returns:
    int: A random integer between 1 and 100.
    """
    return randint(1, 100)

lucky_num = get_rando()

def is_odd(num):
    """
    Check if a number is odd.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is odd, False otherwise.
    """
    if num % 2 == 1:
        return True
    else:
        return False

print(is_odd(13))
print(is_odd(get_rando()))

if __name__ == "__main__":
    print(is_odd(27))
