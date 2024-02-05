from typing import Dict, Tuple


def find_power_sum(
    X: int, n: int, limit: int, memo: Dict[Tuple[int, int], int]
) -> int:
    # Write your code here
    # start with base cases
    # if X is 0, only 1 valid combination possible
    # 0 = 0^n
    if X == 0:
        return 1

    # if X is negative or exponent is 0 or negative, no valid
    # combination is ever possible
    if X < 0 or limit <= 0:
        return 0

    # check if result is in dictionary
    if (X, limit) in memo:
        return memo[(X, limit)]

    # include num in the sum
    include_num = find_power_sum(X - limit**n, n, limit - 1, memo)

    # exclude num from the sum
    exclude_num = find_power_sum(X, n, limit - 1, memo)

    # save the result
    memo[(X, limit)] = include_num + exclude_num

    return memo[(X, limit)]


def power_sum(X: int, n: int) -> int:
    # nth root
    root = X ** (1 / n)

    # largest integer such that m^n <= X
    limit = int(root)

    # create memoization dictionary
    memo = {}

    return find_power_sum(X, n, limit, memo)


def test_power_sum():
    """Test for power_sum function."""
    assert power_sum(10, 2) == 1
    assert power_sum(100, 2) == 3
    assert power_sum(100, 3) == 1
    assert power_sum(800, 2) == 561
    assert power_sum(1000, 10) == 0
    assert power_sum(400, 2) == 55


test_power_sum()
