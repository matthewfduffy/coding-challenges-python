# 12. Given an array, shift values forward by one, dropping the first value and leaving an extra '0' value at the end.

# For Testing:
# Create an array
arr = [n for n in range(1, 15, 2)]
# print(arr)
# Input: [1, 3, 5, 7, 9, 11, 13]
# Output: [3, 5, 7, 9, 11, 13, 0]


# Option 1 - using .pop and .append():

arr.pop(0)
arr.append(0)

print(arr)