from cmath import phase

number = input().split('+')
number[1] = number[1].split('j')[0]
number = complex(int(number[0]), int(number[1]))

print(abs(number))
print(phase(number))
