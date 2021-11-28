# Given an array, square each value in the array

# Create Array
arr = [n for n in range(1, 13)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Option 1 - using a new array:
my_arr = []
for num in arr:
    my_arr.append(num * num)

print(my_arr)


# Option 2 - using map() with lambda:
num_arr_squared = list(map(lambda x: x*x, arr))
print(num_arr_squared)