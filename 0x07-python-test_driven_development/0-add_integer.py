#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that add two integers.

    Parameter:
    a (int or float): The first Number.
    b (int or float, optional): The second number, Defaults To 98.

    Returns:
    int: The sum of a and b, after casting them to integers if necessary.

    Raises:
    TypeError: If neither a nor b is an integer or a float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
