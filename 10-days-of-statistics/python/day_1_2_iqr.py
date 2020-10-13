from statistics import median


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
    return q_n


len_nums = int(input())
nums = list(map(lambda x: int(x), input().rstrip().split()))
freqs = list(map(lambda x: int(x), input().rstrip().split()))

list_ints = []
for i in range(len_nums):
    list_ints += freqs[i] * [nums[i]]

iqr = float(quartile(list_ints, 3) - quartile(list_ints, 1))
print(iqr)
