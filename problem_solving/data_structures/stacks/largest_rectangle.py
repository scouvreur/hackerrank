from typing import List


def largest_rectangle(heights: List[int]) -> int:
    # initialise values
    largest_rectangle_area = 0
    prev_min_height = 0

    return largest_rectangle_recursive(
        heights, prev_min_height, largest_rectangle_area
    )


def largest_rectangle_recursive(
    heights: List[int], prev_min_height: int, largest_rectangle_area: int
) -> int:
    # function with recursive call
    min_height = min(heights)
    rectangle_area = (prev_min_height + min_height) * len(heights)
    largest_rectangle_area = max(largest_rectangle_area, rectangle_area)

    # update prev_min_height
    prev_min_height += min_height

    # remove min_height from all items
    heights = list(map(lambda x: x - min_height, heights))

    # split into new heights
    subheights = split_list_on_zero(heights)

    # repeat for subheights
    for heights in subheights:
        # recursive call
        largest_rectangle_area = largest_rectangle_recursive(
            heights, prev_min_height, largest_rectangle_area
        )

    return largest_rectangle_area


def test_largest_rectangle():
    """Test for largest_rectangle function."""
    assert largest_rectangle([3, 2, 3]) == 6
    assert largest_rectangle([1, 2, 3, 4, 5]) == 9
    assert largest_rectangle([3, 2, 1, 2, 3]) == 5
    assert largest_rectangle([7, 6, 8, 4]) == 18
    assert largest_rectangle([2, 3, 3, 3, 6]) == 12


def split_list_on_zero(array: List[int]) -> List[List[int]]:
    """
    Splits input such as [1, 0, 1] to return [[1], [1]].
    Similar to what .split() would do for a string but for an
    array of integers.
    """
    result_array = []
    current_array = []
    for item in array:
        if item == 0:
            # append only if the array is not empty
            if len(current_array) > 0:
                result_array.append(current_array)
            # if we reach a 0, stop and reset
            current_array = []
        else:
            current_array.append(item)

    # append the final array
    if len(current_array) > 0:
        result_array.append(current_array)

    return result_array


def test_split_list_on_zero():
    """Test for split_list_on_zero function."""
    assert split_list_on_zero([1, 0, 1]) == [[1], [1]]
    assert split_list_on_zero([1, 0, 1, 0, 0, 1]) == [[1], [1], [1]]
    assert split_list_on_zero([1, 0, 1, 1, 0, 1]) == [[1], [1, 1], [1]]


test_split_list_on_zero()
test_largest_rectangle()
