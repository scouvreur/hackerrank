array = [2, 3, 6, 6, 5]

# Sort
array = sorted(array)
# Remove duplicates
array = list(dict.fromkeys(array))

print(array[-2])
