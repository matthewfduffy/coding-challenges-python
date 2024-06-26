"""
    itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B). 

[Task]
You are given a two lists
A and B. Your task is to compute their cartesian product X.

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

[Input Format]

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

[Sample Input]
1 2
3 4

[Sample Output]
(1, 3) (1, 4) (2, 3) (2,4)
"""
from itertools import product

a = map(int, input().split())
b = map(int, input().split())

def cartesian_product(a, b):
    for _ in sorted(set(product(a, b))):
        print(_, end=" ")

cartesian_product(a, b)


# def cartesian_product(a, b):
#     return list(product(a, b))


# Manual Testing
# a = [1, 2]
# b = [3, 4]

# print(cartesian_product(a, b))

