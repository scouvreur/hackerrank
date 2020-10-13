#!/bin/python3

from functools import reduce

array = []
for _ in range(6):
    array.append(list(map(int, input().rstrip().split())))


class Hourglass:
    def __init__(self, items):
        self.items = items

    def view(self):
        print(self.items)

    def sum(self):
        return reduce(lambda x, y: x + y, self.items)


def get_hourglasses(array):
    hourglasses = []
    for i in range(len(array)):
        for j in range(len(array)):
            hourglass = []
            try:
                hourglass.append(array[i][0 + j : 3 + j])
                hourglass.append([array[i + 1][1 + j]])
                hourglass.append(array[i + 2][0 + j : 3 + j])
                hourglass = reduce(list.__add__, hourglass)
                if len(hourglass) == 7:
                    hourglasses.append(Hourglass(hourglass))
                else:
                    pass
            except IndexError:
                pass
    return hourglasses


hourglasses = get_hourglasses(array=array)

sums = []
for hourglass in hourglasses:
    sums.append(hourglass.sum())

print(max(sums))
