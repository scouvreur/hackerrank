n_test_cases = int(input())
for _ in range(n_test_cases):
	d = int(input())

	memo = {
		# n: (fib(n), len(fib(n)))
		0: (0, 1),
		1: (1, 1),
		2: (1, 1)
	}

	def fib(n, memo):
		n = int(n)
		if n in memo:
			return memo[n][0]
		else:
			tmp = fib(n-2, memo) + fib(n-1, memo)
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
