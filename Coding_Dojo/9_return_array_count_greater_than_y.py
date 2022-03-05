#   9. Given an array, return the count that is greater than Y

# Create Array
arr = [n for n in range(1, 13)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Option 1:
y = input("Enter any whole number: ")
count = 0

for num in arr:
    if num > int(y):
        count += 1

print(count)