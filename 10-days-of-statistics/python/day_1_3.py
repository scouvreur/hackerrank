from functools import reduce

n = int(input())
data = list(map(int, input().split()))


def mean(data):
    sum = reduce(lambda x, y: x + y, data)
    return sum / len(data)


def stdev(data):
    mu = mean(data)
    sq_sq_dists_mean = list(map(lambda x: (x - mu) ** 2, data))
    sum_sq_dists_mean = reduce(lambda x, y: x + y, sq_sq_dists_mean)
    return round((sum_sq_dists_mean / len(data)) ** 0.5, 1)


print(stdev(data))
