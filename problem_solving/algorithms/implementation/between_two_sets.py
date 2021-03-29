#!/bin/python3

from typing import List


# Complete the 'get_total_x' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def get_total_x(a: List[int], b: List[int]) -> int:
    # Write your code here
    return None


def test_get_total_x():
    """Test for get_total_x function."""
    assert get_total_x(a=[2, 6], b=[24, 36]) == 2
    assert get_total_x(a=[3, 4], b=[24, 48]) == 2
    assert get_total_x(a=[2, 4], b=[16, 32, 96]) == 3


test_get_total_x()
# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
# arr = list(map(int, input().rstrip().split()))
# brr = list(map(int, input().rstrip().split()))
# total = get_total_x(arr, brr)
# print(total)
