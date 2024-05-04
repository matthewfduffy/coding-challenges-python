"""
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
"""
def find_average(numbers):
    return 0 if numbers == [] else sum(numbers) / len(numbers)


test_a = [1, 3, 5, 7, 9]
test_b = [2, 2, 2]
test_c = []

print(find_average(test_a))
print(find_average(test_b))
print(find_average(test_c))