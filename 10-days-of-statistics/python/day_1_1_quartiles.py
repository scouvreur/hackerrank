def median(numbers):
    """
    Parameters
    ----------
    numbers : list
        a list of numbers

    Returns
    -------
    median : double
        the median of the list of numbers passed
    """
    numbers.sort()
    if len(numbers) % 2 == 1:
        median = numbers[-round(-len(numbers) / 2)]
        median = round(median, 1)
    else:
        median = (
            numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2 - 1)]
        ) / 2
        median = round(median, 1)
    return median


def quartile(list_ints, n):
    """
    Function calculating the quartile of
    a list of integers.

    Parameters
    ----------
    list_ints : list[int]
        List of integers to

    n : int
        Number of the quartile (1st, 2nd, 3rd)
    """
    if n not in [1, 2, 3]:
        msg = "Please enter value between 1 and 3."
        raise ValueError(msg)

    list_ints.sort()
    lower_half = list_ints[: int(len(list_ints) / 2)]

    if len(list_ints) % 2 == 1:
        upper_half = list_ints[int(len(list_ints) / 2 + 1) :]
    else:
        upper_half = list_ints[int(len(list_ints) / 2) :]

    if n == 2:
        q_n = median(list_ints)
    elif n == 1:
        q_n = median(lower_half)
    elif n == 3:
        q_n = median(upper_half)
    return int(q_n)


list_ints_len = int(input())
list_ints = list(map(lambda x: int(x), input().rstrip().split()))

for i in range(1, 4):
    print(quartile(list_ints, i))
