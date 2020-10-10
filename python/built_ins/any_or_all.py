_, list_ints = int(input().strip()), list(map(int, input().strip().split(' ')))
print(all(list(map(lambda x: x>0, list_ints))) and any(list(map(lambda x: str(x) == str(x)[::-1], list_ints))))
