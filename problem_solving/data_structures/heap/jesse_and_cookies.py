from heapq import heapify, heappop, heappush


def cookies(threshold, sweetness_values):
    heapify(sweetness_values)
    num_operations = 0

    # sweetness_values[0] = min(sweetness_values)
    while len(sweetness_values) > 1 and sweetness_values[0] < threshold:
        least_sweet = heappop(sweetness_values)
        second_least_sweet = heappop(sweetness_values)
        heappush(sweetness_values, least_sweet + 2 * second_least_sweet)
        num_operations += 1

    if num_operations > 0 and sweetness_values[0] < threshold:
        return -1
    else:
        return num_operations


def test_cookies():
    """Test for the cookies function."""
    assert cookies(9, [2, 7, 3, 6, 4, 6]) == 4
    assert cookies(7, [1, 2, 3, 9, 10, 12]) == 2
    assert cookies(9, [1, 62, 14]) == 1
    assert cookies(105_823_341, [1] * 100_000) == 99_999


test_cookies()
