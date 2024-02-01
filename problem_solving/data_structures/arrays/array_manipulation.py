from typing import List


def array_manipulation_naive(n: int, queries: List[int]) -> int:
    """
    Naive O(n) implementation.

    Example:
    n = 5
    query = [1, 3, 100]
    array = [0, 100,   0,   0, 0]
            [0, 100, 100,   0, 0]
            [0, 100, 100, 100, 0]
    """
    array = [0] * n

    for a, b, k in queries:
        for index in range(a - 1, b):
            array[index] += k

    return max(array)


def array_manipulation_sparse_array(n: int, queries: List[int]) -> int:
    """
    Implementation using prefix sum or difference array and a sparse array.

    Example:
    n = 5
    query = [1, 3, 100]
    diff_array =     [0, 100,   0,   0,    0]
                     [0, 100,   0,   0, -100]
    cumulative sum = [0, 100, 100, 100,    0]
    """
    diff_array = [0] * n

    for a, b, k in queries:
        diff_array[a - 1] += k
        # edge case when b is at the end of the array
        if b <= n - 1:
            diff_array[b] -= k

    max_value = 0
    cumulative_sum = 0

    for value in diff_array:
        cumulative_sum += value
        max_value = max(max_value, cumulative_sum)

    return max_value


def array_manipulation_hashmap(n: int, queries: List[int]) -> int:
    """
    Implementation using prefix sum or difference array and a hashmap.

    Example:
    n = 5
    query = [1, 3, 100]
    map = {1: 100, 4: -100}
    cumulative sum = [0, 100, 100, 100, 0]
    """
    map = {}

    for a, b, k in queries:
        map[a - 1] = map.get(a - 1, 0) + k
        if b <= n - 1:
            map[b] = map.get(b, 0) - k

    max_value = 0
    cumulative_sum = 0

    for index in range(n):
        cumulative_sum += map.get(index, 0)
        max_value = max(max_value, cumulative_sum)

    return max_value


def test_array_manipulation():
    """Test for array_manipulation function."""
    # test case 0
    n = 5
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    assert array_manipulation_naive(n, queries) == 200
    assert array_manipulation_sparse_array(n, queries) == 200
    assert array_manipulation_hashmap(n, queries) == 200

    # test case 1
    n = 10
    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1],
    ]
    assert array_manipulation_naive(n, queries) == 10
    assert array_manipulation_sparse_array(n, queries) == 10
    assert array_manipulation_hashmap(n, queries) == 10

    # test case 2
    n = 4
    queries = [[2, 3, 603], [1, 1, 286], [4, 4, 882]]
    assert array_manipulation_naive(n, queries) == 882
    assert array_manipulation_sparse_array(n, queries) == 882
    assert array_manipulation_hashmap(n, queries) == 882


test_array_manipulation()
