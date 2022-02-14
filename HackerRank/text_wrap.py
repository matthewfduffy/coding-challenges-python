# Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=false
"""
Given a string S and width, W. Your task it to wrap into a paragraph of width W

Sample Input:   
    s = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    W = 4

Sample Output:
    ABCD
    EFGH
    IJKL
    MNOP
    QRST
    UVWX
    YZ

"""
def wrap(string, max_width):
    new_str = ""
    counter = 0
    for letter in string:
        new_str += letter
        counter += 1
        if counter == max_width:
            new_str += "\n"
            counter = 0
        
    return new_str


# Testing
print(wrap("ABCDEDGHI", 4))