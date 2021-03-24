#!/bin/python3


def invert_list(numbers):
    """
    Parameters
    ----------
    numbers : list
        a list of numbers

    Returns
    -------
    reversed : list
        the reverse list of numbers passed
    """
    reversed = []
    for i in range(len(numbers)):
        reversed.append(numbers.pop())
    return reversed


if __name__ == "__main__":
    n = int(input())

    array = list(map(lambda x: int(x), input().split()))
    reversed = invert_list(array)
    print(" ".join(map(str, reversed)))
