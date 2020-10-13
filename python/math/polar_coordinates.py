from cmath import phase

number = input()
if "+" in number:
    number = number.split("+")
    number[1] = number[1].split("j")[0]
    number = complex(int(number[0]), int(number[1]))
elif "-" in number:
    if number.count("-") == 1:
        number = number.split("-")
        number[1] = number[1].split("j")[0]
        number = complex(int(number[0]), -int(number[1]))
    elif number.count("-") == 2:
        number = number.split("-")
        number[2] = number[2].split("j")[0]
        number = complex(-int(number[1]), -int(number[2]))

print(abs(number))
print(phase(number))
