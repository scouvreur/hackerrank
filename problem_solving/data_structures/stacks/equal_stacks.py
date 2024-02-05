from typing import List


def equal_stacks(h1: List[int], h2: List[int], h3: List[int]) -> int:
    # Write your code here
    # reverse the stacks
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    # calculate the cumulative sums
    h1_cumsum = calculate_cumulative_sum(h1)
    h2_cumsum = calculate_cumulative_sum(h2)
    h3_cumsum = calculate_cumulative_sum(h3)

    # find the intersection between the 3 sets
    # using & operator
    common = set(h1_cumsum) & set(h2_cumsum) & set(h3_cumsum)
    # using the .intersection() method from set()
    # common = set(h1_cumsum).intersection(set(h2_cumsum)).intersection(set(h3_cumsum))
    # both operations are O(min(len(set1), len(set2)))

    if len(common) > 0:
        return max(common)
    else:
        return 0


def test_equal_stacks():
    """Test for equal_stacks function."""
    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]
    assert equal_stacks(h1, h2, h3) == 5


def calculate_cumulative_sum(array: List[int]) -> List[int]:
    result = []
    cumulative_sum = 0
    for value in array:
        cumulative_sum += value
        result.append(cumulative_sum)

    return result


def test_calculate_cumulative_sum():
    """Test for calculate_cumulative_sum function."""
    assert calculate_cumulative_sum([1, 1, 1, 2, 3]) == [1, 2, 3, 5, 8]


test_calculate_cumulative_sum()
test_equal_stacks()
