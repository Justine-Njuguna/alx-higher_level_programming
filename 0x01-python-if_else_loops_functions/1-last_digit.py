#!/usr/bin/python3
import random


def generate_random_number():
    """
    Generate a random number between -10000 and 10000.

    Returns:
    - The generated random number
    """
    return random.randint(-10000, 10000)


def get_last_digit(number):
    """
    Get the last digit of a number.

    Args:
    - number: the input number

    Returns:
    - The last digit of the number
    """
    return abs(number) % 10


def print_last_digit_info(number, last_digit):
    """
    Print information about the last digit of a number.

    Args:
    - number: the original number
    - last_digit: the last digit of the number
    """
    if number < 0:
        last_digit = -last_digit

    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print("Last digit of {0} is {1} and is 0".format(number, last_digit))
    else:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")


if __name__ == "__main__":
    random_number = generate_random_number()
    last_digit = get_last_digit(random_number)
    print_last_digit_info(random_number, last_digit)
