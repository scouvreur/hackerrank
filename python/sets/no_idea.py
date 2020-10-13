n = 3
m = 2
array = [1, 5, 3]
A = set([3, 1])
B = set([5, 7])

happiness = 0
for item in array:
    if item in A:
        happiness += 1
    if item in B:
        happiness -= 1

print(happiness)
