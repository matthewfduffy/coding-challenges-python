"""
This tool returns the r-length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
"""
"""
[Task]

You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

[Input Format]
A single line containing the string S and integer value K separated by a space.

[Constraints]
The string contains only UPPERCASE characters.

[Output Format]
Print the different combinations of string S on separate lines.

[Sample Input]
HACK 2

[Sample Output]
A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations

def combination_finder(x, y):
    # print(list(combinations(x, y)))
    array = list(combinations(x, y))
    for letter in range(len(x)):
        print(x)
        letter += 1
    for combo in array:
        print(combo)




combination_finder('HACK', 2)