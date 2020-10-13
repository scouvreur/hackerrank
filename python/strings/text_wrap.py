def wrap(string, max_width):
    """
    Takes in a string of length n and an integer
    max_width < n, and returns the string wrapped
    with lines no longer then max_width chars.

    Parameters
    ----------
    string : string
        Input string.

    max_width : int
        Max number of chars before inserting
        newline.

    Returns
    -------
    result : string
        Wrapped string.
    """
    result = ""
    for i in range(len(string)):
        try:
            result += string[i * max_width : (i + 1) * max_width] + "\n"
        except IndexError:
            result += string[i * max_width :]
    return result


string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
result = wrap(string, max_width)
print(result)
