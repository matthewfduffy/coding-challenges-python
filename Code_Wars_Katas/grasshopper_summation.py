"""
Grasshopper Summation

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

For example (Input -> Output):
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
"""
# Option 1
def sum_to_zero(n):
	result = 0
	for num in range(n, 0, -1):
		result += num
	return result

# print(sum_to_zero(8))

# Option 2 - Recursion
def sum_to_num(n):
    if n == 1:
        return n
    else:
		# print(f"The current value of n is: {n}")
	    return n + sum_to_num(n-1)

print(sum_to_num(8))