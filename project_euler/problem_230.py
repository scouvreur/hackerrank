
# line = "1415926535 8979323846 35".split()
line = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 104683731294243150".split()

n = int(input())
for _ in range(n):
	line = input().split()

	# base cases
	bcs = {
		"A" : (len(line[0]), line[0]),
		"B" : (len(line[1]), line[1])
	}
	d = int(line[2])
	memo = {0: "A", 1: "B"}

	def fib(n, memo):
		n = int(n)
		if n in memo:
			return memo[n]
		else:
			memo[n] = fib(n-2, memo) + fib(n-1, memo)
			return memo[n]

	def len_fib(n, memo, bcs):
		n = int(n)
		len_fib = 0
		for char in fib(n, memo):
			len_fib += bcs[char][0]
		return len_fib

	def AB_to_real_string(n, memo, bcs):
		n = int(n)
		real_string = ""
		for char in fib(n, memo):
			real_string += bcs[char][1]
		return real_string

	def fib_digit(d, memo, bcs):
		d = int(d)
		n = 0
		while True:
			n += 1
			if len_fib(n, memo, bcs) > d:
				a = AB_to_real_string(n, memo, bcs)
				print(a[d-1])
				break

	fib_digit(d, memo, bcs)
