def merge_the_tools(string, k):
    """
    Takes in a string of length n and an integer k
    always multiple of n, and returns k subsets with
    unique characters.

    Parameters
    ----------
    string : string
        Input string.

    k : int
        Factor of len(string) to cut into subsets.

    Returns
    -------
    subsets : list[string]
        List of k subsets.
    """
    subsets = []
    for i in range(k):
        subsets.append(string[int(i * k) : int((i + 1) * k)])

    for subset in subsets:
        temp = list(dict.fromkeys(list(subset)))
        subset = ""
        for char in temp:
            subset += char
        print(subset)
    return subsets


string, k = "AABCAAADA", 3
merge_the_tools(string, k)
