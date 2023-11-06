from typing import List


def minimum_bribes(q: List[int]) -> str:
    total_bribes = 0
    for i, new_position in enumerate(q):
        # if a number advanced more than 2 positions
        # it must have bribed more than twice
        original_position = i + 1
        positions_advanced = new_position - original_position
        if positions_advanced > 2:
            return "Too chaotic"

        # if a number with a value greater than me
        # is up to 2 places in front
        # i must have been bribed by them
        for item in q[max(new_position - 2, 0) : original_position - 1]:
            if item > new_position:
                total_bribes += 1

    return str(total_bribes)


def test_minimum_bribes():
    """Test for minimum_bribes function."""
    assert minimum_bribes([1, 2, 3, 5, 4, 6, 7, 8]) == "1"
    assert minimum_bribes([4, 1, 2, 3]) == "Too chaotic"
    assert minimum_bribes([2, 1, 5, 3, 4]) == "3"
    assert minimum_bribes([2, 5, 1, 3, 4]) == "Too chaotic"
    assert minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6]) == "4"
    assert minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]) == "7"


test_minimum_bribes()
