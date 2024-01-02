#!/usr/bin/python3

def pow(a, b):
    """
    Computes the value of a ^ b.

    Args:
    - a: base
    - b: exponent

    Returns:
    - The value of a ^ b
    """
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    for _ in range(b):
        result *= a

    return result  # Return the unrounded result


if __name__ == "__main__":
    print(round(pow(2, 2), 10))  # Round after calculation
    print(round(pow(98, 2), 10))
    print(pow(98, 0))
    print(round(pow(100, -2), 10))
    print(pow(-4, 5))
    print(round(pow(10, -2), 10))
    print(round(pow(-98, -10), 10))  # Correct output: 1.223881142011411e-20
