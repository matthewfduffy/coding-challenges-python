# Create and return an array with odd integers from 1-255

# Option 1:
arr = []
num = 1
while num <= 255:
    arr.append(num)
    num += 2

print(arr)


# Option 2 - List Comprehension:
arr1 = [val for val in range(1, 256, 2)]
print(arr1)