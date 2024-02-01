from typing import List


def rotate_left(d: int, array: List[int]) -> List[int]:
    return array[d:] + array[:d]


def test_rotate_left():
    """Test for the rotate_left function."""
    assert rotate_left(2, [1, 2, 3, 4, 5]) == [3, 4, 5, 1, 2]


test_rotate_left()
