# Find a String
# Given a string and sub-string, return an integer indicating the number of occurrences of the substring in the original string
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
# Ex.   [Input_1] ABCDCDC
#       [Input_2] CDC
#       [Output]    2

"""
NOT COMPLETE
"""

def count_substring(string, substring):
    count = 0
    x = 0
    while st<=len(string):
        st = string.find(substring,st)
        if st!=-1:
            count+=1
            st+=1
        else: break
        
    return count
