# Given an array, replace negative values with 'Dojo'

arr = [n for n in range(-15, 15, 2)]    # [-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13]


# Option 1 using a new aray:
new_arr = []

for num in arr:
    if num < 0:
        new_arr.append('Dojo')
    else:
        new_arr.append(num)

print(new_arr)