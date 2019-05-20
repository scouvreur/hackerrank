def is_leap(year):
    year = int(year)
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
