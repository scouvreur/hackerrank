from functools import reduce

n = int(input())
data = list(map(int, input().split()))
weights = list(map(int, input().split()))


def weighted_sum(data, weights):
    assert len(data) == len(weights)
    sum_weights = reduce(lambda x, y: x + y, weights)
    cumsum = 0
    for i in range(len(data)):
        cumsum += data[i] * weights[i]
    return round(cumsum / sum_weights, 1)


print(weighted_sum(data, weights))
