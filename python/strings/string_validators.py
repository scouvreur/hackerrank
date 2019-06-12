string = input()

alnum = []
alpha = []
digit = []
lower = []
upper = []

for char in string:
    if char.isalnum():
        alnum.append(1)

    if char.isalpha():
        alpha.append(1)

    if char.isdigit():
        digit.append(1)

    if char.islower():
        lower.append(1)

    if char.isupper():
        upper.append(1)

print(sum(alnum) >= 1)
print(sum(alpha) >= 1)
print(sum(digit) >= 1)
print(sum(lower) >= 1)
print(sum(upper) >= 1)
