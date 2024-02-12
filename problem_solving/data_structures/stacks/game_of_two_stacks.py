from typing import List


def two_stacks_naive(max_sum: int, a: List[int], b: List[int]):
    # Reverse order of a and b
    a = a[::-1]
    b = b[::-1]

    current_sum = 0
    num_selections = 0

    while (current_sum + a[-1] <= max_sum) or (current_sum + b[-1] <= max_sum):
        # Check which item from the top of both stacks is greater
        if a[-1] < b[-1]:
            current_sum += a.pop()
        else:
            current_sum += b.pop()

        num_selections += 1

    return num_selections


def two_stacks(max_sum: int, a: List[int], b: List[int]):
    # Start 2 cursors for a and b
    a_index = 0
    b_index = 0

    current_sum = 0
    num_selections = 0

    # Select all from a one by one until the maximum is reached
    while a_index < len(a) and current_sum + a[a_index] <= max_sum:
        current_sum += a[a_index]
        a_index += 1

    num_selections = a_index
    max_num_selections = a_index

    # Decrement the a cursor by 1
    a_index -= 1

    while b_index < len(b):
        # Case where there are still items from b we could add
        if current_sum + b[b_index] <= max_sum:
            current_sum += b[b_index]
            b_index += 1
            num_selections += 1
            # If current number of selections greater than max, update max
            max_num_selections = max(max_num_selections, num_selections)
        # Case when nothing can be added from b, see if by removing something
        # selected from a allows to get an extra item from b
        elif a_index >= 0:
            current_sum -= a[a_index]
            a_index -= 1
            num_selections -= 1
        # If we can't add anything from b and nothing from a, stop
        else:
            break

    return max_num_selections


def test_two_stacks():
    """Test for two_stacks function."""
    max_sum = 10
    a = [4, 2, 4, 6, 1]
    b = [2, 1, 8, 5]
    assert two_stacks_naive(max_sum, a, b) == 4
    assert two_stacks(max_sum, a, b) == 4


test_two_stacks()
