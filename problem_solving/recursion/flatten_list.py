#!/bin/python3


def flatten_list(nested_list: list) -> list:
    flattened_list = []
    for item in nested_list:
        if isinstance(item, int):
            flattened_list.append(item)
        else:
            flattened_list.extend(flatten_list(item))
    return flattened_list


def test_flatten_list():
    """Test for flatten list function."""
    assert flatten_list([1, [2], [[3], 4, [[5]]]]) == [1, 2, 3, 4, 5]
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[[[[]]]], [1, [[2]]]]) == [1, 2]


test_flatten_list()
