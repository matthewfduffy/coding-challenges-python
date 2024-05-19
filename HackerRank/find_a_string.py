# Find a String
# Given a string and sub-string, return an integer indicating the number of occurrences of the substring in the original string
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
# Ex.   [Input_1] ABCDCDC
#       [Input_2] CDC
#       [Output]    2

"""
NOT COMPLETE
"""
import re

def count_substring(string1, sub_string1):
    string_lst = list(string1)
    sub_string_lst = list(sub_string1)
    condition = len(string1)
    counter = 0
    x = 0
    y = 0

    while condition >= len(sub_string1):
        if sub_string_lst[x] != string_lst[y]:
            condition = condition - 1
            y += 1
        else:
            condition = condition - 1
            x += 1
            y += 1
        counter += 1
        # print (counter, sub_string_lst[x], string_lst[y])
    return counter




    # pattern = "[" + sub_string + "]"
    # # print(pattern)
    # x = re.findall(pattern, string)
    # if len(sub_string) == len(x):
    #     return 1
    # elif len(sub_string) > len(x):
    #     return 0
    # else:
    #     return len(x) % len(sub_string)
    
# print(5 % 3)
    # if len(x) - len(pattern) == 0:
    #     print(len(x), len(pattern))
    # else:
    #     return len(x) - len(pattern)
    # str_lst = []
    # sub_str_lst = []
    # counter = 0
    # index = 1

    # for letter in string:
    #     str_lst.append(letter)
    # for key_letter in sub_string:
    #     sub_str_lst.append(key_letter)
    # print(str_lst)
    # print(sub_str_lst)

    # while len(str_lst > 0):
    #     if str_lst[0] != sub_str_lst[0]:
    #         del str_lst[0]
    #     elif str_lst[0]

# Test Cases
print(count_substring("ABCDCDC", "CDC"))