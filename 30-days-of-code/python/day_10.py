#!/bin/python3


def convert_base2(n):
    """This function takes an integer as input and returns
    a string with it's binary representation.

    Parameters
    ----------
    n : int
        Integer in base 10 to convert.

    Returns
    -------
    n_base2 : string
        String representation of n in base 2.
    """
    n_base2 = ""
    temp = n
    while temp != 0:
        y = temp % 2
        temp = temp // 2
        n_base2 += str(y)
    # Reverse n_base2 string
    n_base2 = n_base2[::-1]
    return n_base2


def max_n_consecutive_1s(binary_str):
    """This function takes a number's binary representation
    and return the maximum number of consecutive 1 digits in the
    string.

    Parameters
    ----------
    binary_str : str
        Binary representation of an integer.

    Returns
    -------
    max_n_1s : int
        Maximum number of consecutive 1 digits in the string.
    """
    ones = binary_str.split("0")
    max_n_1s = max(list(map(lambda x: len(x), ones)))
    return max_n_1s


n = int(input())
print(max_n_consecutive_1s(convert_base2(n)))
