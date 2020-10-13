n_test_cases = int(input())
for _ in range(n_test_cases):
    d = int(input())

    memo = {
        # n: (fib(n), len(fib(n)))
        0: (0, 1),
        1: (1, 1),
        2: (1, 1),
    }

    def fib(n, memo):
        n = int(n)
        phi = (1 + 5 ** 0.5) / 2
        if n in memo:
            return memo[n][0]
        else:
            tmp = int(round((phi ** n) / (5 ** 0.5)))
            memo[n] = (tmp, len(str(tmp)))
            return memo[n][0]

    n = 0
    while True:
        fib(n, memo)
        if memo[n][1] >= d:
            print(n)
            break
        else:
            n += 1
