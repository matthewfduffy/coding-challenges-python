# Given an array, print max, min, and average values

# Create an array
arr = [n for n in range(1, 15, 2)]
# print(arr)
# [1, 3, 5, 7, 9, 11, 13]

# Option 1:
sub_arr = sorted(arr)
arr_max = sub_arr[-1]
arr_min = sub_arr[0]
arr_avg = (sum(sub_arr) / len(sub_arr))

output = (f"The max number in array is: {arr_max}. \n\t The smallest number is: {arr_min}. \n\t The average of the array is: {arr_avg}.")

print(output)