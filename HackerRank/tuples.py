"""
Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t)

[Input Format]

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

[Output Format]
Print the result of hash(t)

[Sample Input]
2
12

[Sample Output]
3713081631934410656
"""

# Run using pypy 3

n = int(input())
t = tuple(map(int, input().split()))
result = hash(t)
print(result)