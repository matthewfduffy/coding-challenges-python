# Largest Number
# https://app.codesignal.com/arcade/code-arcade/intro-gates/SZB5XypsMokGusDhX

"""
Given an integer n, return the largest number that contains exactly n digits

Sample Input:
    2

Sample Output:
99
"""

def largestNumber(n):
    lookup = {
        1: 9,
        2: 99,
        3: 999,
        4: 9999,
        5: 99999,
        6: 999999,
        7: 9999999,
        8: 99999999,
        9: 999999999,
    }

    return lookup[n]


print(largestNumber(2))
print(largestNumber(3))
