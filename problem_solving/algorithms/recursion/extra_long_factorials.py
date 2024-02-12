from typing import Dict


def extra_long_factorials(n: int):
    # Write your code here
    memo = {}
    return factorial(n, memo)


def factorial(n: int, memo: Dict[int, int]) -> int:
    # Define base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Check if factorial is in dictionary
    if n in memo:
        return memo[n]
    # If not in dictionary, make recursive call
    else:
        return n * factorial(n - 1, memo)


def test_extra_long_factorials():
    """Test for extra_long_factorials function."""
    assert extra_long_factorials(25) == 15511210043330985984000000
    assert extra_long_factorials(30) == 265252859812191058636308480000000
    assert (
        extra_long_factorials(45)
        == 119622220865480194561963161495657715064383733760000000000
    )
    assert (
        extra_long_factorials(52)
        == 80658175170943878571660636856403766975289505440883277824000000000000
    )


test_extra_long_factorials()
