class NegativeValueError(Exception):
    """Raised when the input value is negative"""

    pass


class Calculator:
    def __init__(self):
        pass

    def power(self, n, p):
        try:
            if n < 0 or p < 0:
                raise NegativeValueError
            else:
                return n**p
        except NegativeValueError:
            return "n and p should be non-negative"


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
