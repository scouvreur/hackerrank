def matching_strings(string_list, queries):
    # Write your code here
    hits = [0] * len(queries)

    for index, query in enumerate(queries):
        for string in string_list:
            if query == string:
                hits[index] += 1

    return hits


def test_matching_strings():
    """Test for matching_strings function."""
    string_list = [
        "aba",
        "baba",
        "aba",
        "xzxb",
    ]

    queries = [
        "aba",
        "xzxb",
        "ab",
    ]

    assert matching_strings(string_list, queries) == [2, 1, 0]


if __name__ == "__main__":
    test_matching_strings()
