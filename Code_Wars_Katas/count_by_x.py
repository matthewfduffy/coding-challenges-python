"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
Examples

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""
# Option 1
def count_by(x, n):
    return_array = [x]
    for i in range(n-1):
        return_array.append(return_array[-1] + x)
    return return_array



# Option 2
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
    # OR
    return list(range(x, x * n + 1, x))



print(count_by(1,10))
print(count_by(2,5))
