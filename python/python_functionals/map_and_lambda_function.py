cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    """
    Returns a list of fibonacci numbers of length n

    Parameters
    ----------
    n : int
        Number in fibonacci suite desired

    Returns
    -------
    fib_list : list[ints]
        List of integers
    """
    memo = [0, 1]

    for i in range(2, n):
        memo += [memo[i - 2] + memo[i - 1]]

    return memo[:n]


print(fibonacci(5))
