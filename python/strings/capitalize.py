name = "chris alan"
name = name.title()

name = "1 w 2 r 3g"

# Complete the solve function below.
def solve(string):
    """
    Capitalizing function
    """
    list_strings = string.rstrip().split(" ")
    result = ""
    for item in list_strings:
        if item[0].isalpha():
            item = item.title()

        result += item + " "
    return result.strip()
