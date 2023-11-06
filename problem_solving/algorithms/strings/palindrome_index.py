def palindrome_index(s):
    # case when string already is a palindrome
    if s == s[::-1]:
        return -1

    # logic for other cases
    n = len(s)
    for i in range(n // 2):
        left_index = i
        right_index = n - 1 - i
        # check if first and last are different
        if s[left_index] != s[right_index]:
            if s[left_index:right_index] == s[left_index:right_index][::-1]:
                return right_index
            elif (
                s[left_index + 1 : right_index + 1]
                == s[left_index + 1 : right_index + 1][::-1]
            ):
                return left_index

    return -1


def test_palindrome_index():
    """Test for palindrome_index function."""
    assert palindrome_index("aaab") == 3
    assert palindrome_index("baa") == 0
    assert palindrome_index("aaa") == -1
    assert palindrome_index("quyjjdcgsvvsgcdjjyq") == 1 # 8 is also a solution
    assert palindrome_index("lhrxvssvxrhl") == -1


test_palindrome_index()
