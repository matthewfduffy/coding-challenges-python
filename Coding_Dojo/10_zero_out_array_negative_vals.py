# 10. Given an array, set negative values to zero

# Create Array
arr = [n for n in range(-20, 20, 5)]
# [-20, -15, -10, -5, 0, 5, 10, 15]


# Option 1 - without function
index = 0
for num in arr:
    if num < 0:
        arr[index] = 0
    index += 1
print(arr)


# Option 2 - with function
def zero_out_negatives(arr):
    index = 0
    for num in arr:
        if num < 0:
            arr[index] = 0
        index += 1
    return arr

print(zero_out_negatives(arr))