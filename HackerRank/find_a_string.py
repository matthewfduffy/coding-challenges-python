# Find a String
# Given a string and sub-string, return an integer indicating the number of occurrences of the substring in the original string
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
# Ex.   [Input_1] ABCDCDC
#       [Input_2] CDC
#       [Output]    2

import re

def count_substring(string, sub_string):
    pattern = "[" + sub_string + "]"
    print(pattern)
    x = re.findall(pattern, string)
    print(x)
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