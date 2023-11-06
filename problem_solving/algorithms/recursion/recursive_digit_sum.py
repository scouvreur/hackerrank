def digit_sum(n: str) -> int:
    return sum(list(map(lambda x: int(x), list(n))))


def super_digit(n: str, k: int) -> int:
    substring_super_digit = 0
    while len(n) > 1:
        substring_super_digit = digit_sum(n)
        n = str(substring_super_digit)

    super_digit = (substring_super_digit * k) % 9
    if super_digit == 0:
        return 9
    else:
        return super_digit


def test_digit_sum():
    """Test for digit_sum function."""
    assert digit_sum("9875") == 29
    assert digit_sum("116") == 8


def test_super_digit():
    """Test for super_digit function."""
    assert super_digit("9875", 1) == 2
    assert super_digit("9875", 4) == 8
    assert super_digit("148", 3) == 3
    assert super_digit("123", 3) == 9
