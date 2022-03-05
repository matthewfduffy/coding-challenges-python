#   6. analyze an array's values and print the average

arr = [2, 6, 13, 15, 32, -9, 10]

# Option 1 - without built-ins:
sum = 0
for num in arr:
    sum += num

print(sum / len(arr))