def is_balanced(s):
    stack = []
    close_to_open_brackets = {"}": "{", "]": "[", ")": "("}

    for index, char in enumerate(s):
        if char in close_to_open_brackets:
            if len(stack) == 0:
                return "NO"
            elif close_to_open_brackets[char] == stack[-1]:
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(char)

    if len(stack) > 0:
        return "NO"
    else:
        return "YES"


def test_is_balanced():
    """Test for is_balanced function."""
    assert is_balanced("}{[()]}") == "NO"
    assert is_balanced("{[()]}") == "YES"
    assert is_balanced("{[(])}") == "NO"
    assert is_balanced("{{[[(())]]}}") == "YES"
    assert is_balanced("{{[(){}]}}") == "YES"
    assert is_balanced("{(([])[])[]]}") == "NO"


test_is_balanced()
