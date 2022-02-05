# Super Reduce String
# https://www.hackerrank.com/challenges/reduced-string/problem

"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return `Empty String`

[Sample Input -> Output]:
    s = 'aab' -> 'b'
    s = 'aaabccddd' -> 'abd'
    s = 'aa' -> 'Empty String'

"""
#TODO: Refactor to account for edge cases. Current solution doesn't account for non-matching characters that are separated from the same character matching set 
from collections import Counter

def superReducedString(s):
    str_lst = list(s)
    item_count = Counter(str_lst)

    new_str =""
    for key, value in item_count.items():
        if value % 2 == 0:
            pass
        else:
            new_str += key

    if new_str == "":
        new_str = "Empty String"

    return new_str