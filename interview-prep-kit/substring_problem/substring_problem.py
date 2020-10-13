def is_perfect(substring, k):
    """
    Given a substring, determines if it is perfect.

    Returns
    -------
    perfect: bool
        Whether substring is perfect or not.
    """
    counts = {}
    for i in range(10):
        counts[i] = substring.count(str(i))
    # remove counts with value 0
    counts = {key: val for key, val in counts.items() if val != 0}
    perfect = all(value == k for value in counts.values())
    return perfect


def test_is_perfect():
    # Test for is_perfect function
    assert is_perfect(substring="102012", k=2)
    assert is_perfect(substring="22", k=2)
    assert not is_perfect(substring="220", k=2)
    assert is_perfect(substring="212211", k=3)
    assert is_perfect(substring="122112", k=3)
    assert is_perfect(substring="221121", k=3)


def get_all_mod_k_substrings(s, k):
    """
    If k is 3 for instance, will return substrings of
    length 3, 6, 9 etc.

    Returns
    -------
    substrings: [str]
        List of all possible substrings.
    """
    substrings = []
    i = 1
    while i * k <= len(s):
        for j in range(len(s)):
            substring = s[j : j + k * i]
            if len(substring) == k * i:
                substrings.append(substring)
        i += 1
    return substrings


def test_get_all_mod_k_substrings():
    # Test for get_all_mod_k_substrings function
    ground_truth = [
        "10",
        "02",
        "20",
        "01",
        "12",
        "22",
        "1020",
        "0201",
        "2012",
        "0122",
        "102012",
        "020122",
    ]
    assert ground_truth == get_all_mod_k_substrings(s="1020122", k=2)


# Run tests
test_is_perfect()
test_get_all_mod_k_substrings()


def perfectSubstring(s, k):
    # Write your code here
    perfect_substrings = 0
    substrings = get_all_mod_k_substrings(s=s, k=k)
    for string in substrings:
        if is_perfect(substring=string, k=k):
            perfect_substrings += 1
    return perfect_substrings


# test cases
s = "1102021222"
k = 2

s = "1221221121"
k = 3
