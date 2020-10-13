def factorial(n):
    """
    Returns factorial of the integer passed.
    Naive recursive implementation with
    memoization.
    """
    memo = {0: 0, 1: 1}
    # base cases or memoed cases
    try:
        return memo[n]
    except KeyError:
        memo[n] = n * factorial(n - 1)
        return memo[n]


def permutations(n, x):
    """
    Returns possible permutations for
    n over x.
    """
    return factorial(n) / (factorial(x) * (factorial(n - x)))


input = list(map(lambda x: float(x), "1.09 1".rstrip().split()))


# p = input[0] / sum(input)
p = 0.5
q = 1 - p

# n = 6
# x = 3

n = 10
x = 5

b = permutations(n, x) * p ** x * q ** (n - x)
print(b)
