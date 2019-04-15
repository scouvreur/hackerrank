return_date = list(map(lambda x: int(x), input().split()))
due_date = list(map(lambda x: int(x), input().split()))

day = 0
month = 1
year = 2

if return_date[year] > due_date[year]:
    fine = 10000
elif return_date[year] < due_date[year]:
    fine = 0
elif return_date[month] > due_date[month]:
    fine = 500*(return_date[month] - due_date[month])
elif return_date[day] > due_date[day]:
    fine = 15*(return_date[day] - due_date[day])
else:
    fine = 0

print(fine)
