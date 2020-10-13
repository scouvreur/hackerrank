from functools import reduce


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        for d in range(1, n + 1):
            if n % d == 0:
                divisors.append(d)
        return reduce(lambda x, y: x + y, divisors)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
