"""
[adjacentElementsProduct](https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m)

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""
from collections import deque

def adjacentElementsProduct(inputArray):
    largest_sum = -1000
    index = 0

    deq = deque(inputArray)

    while len(deq) > 1:
        x = deq[index] * deq[index + 1]
        deq.popleft()

        if x > largest_sum:
            largest_sum = x

    # print("The largest sum is: ", largest_sum)
    return largest_sum


# inputArray = [3, 6, -2, -5, 7, 3]
# print(adjacentElementsProduct(inputArray))