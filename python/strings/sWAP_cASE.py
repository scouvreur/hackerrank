def swap_case(string):
    """
    This function takes in a string and returns
    a swapped version.

    Parameters
    ----------
    string : string
        The string to swap cases on.

    Returns
    -------
    swapped : string
        The swapped string.
    """
    swapped = ""
    for char in string:
        if char.islower():
            swapped += char.upper()
        else:
            swapped += char.lower()
    return swapped


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
