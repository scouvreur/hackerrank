#!/bin/python3

from typing import List


def get_subarrays(array: List[int]) -> List[List[int]]:
    """
    Function to get subarrays of an array where the maximum
    absolute difference between the elements is 1.

    Parameters
    ----------
    array: List[int]
        Input array of integers.

    Returns
    -------
    """
    # validate input
    try:
        reference = list(map(int, array))
        assert reference == array
    except:
        raise ValueError("Input array must contain integers.")
    return None


def test_get_subarrays():
    """Test for get_subarrays function."""
    assert get_subarrays(array=[1, 1, 2, 2, 4, 4, 5, 5, 5]) == [
        [1, 1, 2, 2],
        [4, 4, 5, 5, 5],
    ]
    assert get_subarrays(array=[4, 6, 5, 3, 3, 1]) == [[3, 3, 4]]
    assert get_subarrays(array=[1, 2, 2, 3, 1, 2]) == [[1, 1, 2, 2, 2]]


test_get_subarrays()
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = len(get_subarrays(a))
print(result)

array = [1, 2, 2, 3, 1, 2]
result = []
for i, _ in enumerate(array):
    try:
        if array[i] - array[i+1] <= 1:
            result.append(array[i])
        else:
            break
    except IndexError:
        break
