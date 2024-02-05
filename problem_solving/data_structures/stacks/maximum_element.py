from typing import List


def get_max_naive(operations: List[str]) -> List[int]:
    """Naive implementation of get_max."""
    stack = []
    answers = []

    for operation in operations:
        type = int(operation.split(" ")[0])
        if type == 1:
            x = int(operation.split(" ")[1])
            stack.append(x)
        elif type == 2:
            stack.pop()
        elif type == 3:
            # get max value of the stack
            # at that moment
            answers.append(max(stack))

    return answers


def get_max(operations: List[str]) -> List[int]:
    """Implementation of get_max using a stack for the max values."""
    stack = []
    answers = []
    max_values = []

    for index, operation in enumerate(operations):
        type = int(operation.split(" ")[0])

        if len(max_values) == 0:
            current_max_value = None
        else:
            current_max_value = max_values[-1]

        if type == 1:
            # parse x and push to the stack
            x = int(operation.split(" ")[1])
            stack.append(x)

            # if there is no value in the
            # max_values, or if x is greater
            # than the current max value push x
            if current_max_value is None or x >= current_max_value:
                max_values.append(x)
        elif type == 2:
            if len(stack) > 0:
                # remove the last number from the stack
                removed = stack.pop()

                # if the item removed is the same as
                # current maximum AND it is the last
                # remaining occurrence, the new maximum
                # becomes the previous
                if removed == current_max_value:
                    max_values.pop()
        elif type == 3:
            if current_max_value is not None:
                answers.append(current_max_value)

        # DEBUG
        # print("-" * 115)
        # print("index:", index)
        # print("type:", type)
        # print("stack:", stack)
        # print("current_max_value:", current_max_value)
        # print("max_values:", max_values)
        # ❯ python maximum_element.py > maximum_element.log

    return answers


def read_file(file_path: str) -> List[str]:
    """Read a text file into a list of strings."""
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines


def read_test_case(file_path: str) -> List[str]:
    """Read a text file into a test case."""
    operations = read_file(file_path)
    expected_len = int(operations[0])
    operations = operations[1:]
    assert expected_len == len(operations)
    return operations


def test_get_max():
    """Test for get_max function."""
    # test case 0
    operations = [
        "1 97",
        "2",
        "1 20",
        "2",
        "1 26",
        "1 20",
        "2",
        "3",
        "1 91",
        "3",
    ]

    assert get_max_naive(operations) == [26, 91]
    assert get_max(operations) == [26, 91]

    # test case 6
    operations = read_test_case("maximum_element_test_case_6_input.txt")
    expected = list(
        map(
            lambda x: int(x),
            read_file("maximum_element_test_case_6_output.txt"),
        )
    )

    assert get_max_naive(operations) == expected
    assert get_max(operations) == expected


test_get_max()
