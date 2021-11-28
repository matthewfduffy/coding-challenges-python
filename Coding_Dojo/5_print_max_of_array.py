#  print the largest element in a given array

arr = [2, 6, 13, 15, 32, -9, 10]

# option 1
largest_num = 0

for num in arr:
    if num > largest_num:
        largest_num = num
print(largest_num)



# option 2
sorted_arr = arr
sorted_arr.sort()
print(sorted_arr[-1])

