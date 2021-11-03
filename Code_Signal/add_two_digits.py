# Add Two Digits
# https://app.codesignal.com/arcade/code-arcade/intro-gates/wAGdN6FMPkx7WBq66

""" 
You are given a two-digit integer n. 
Return the sum of it's digits

Sample Input:
    29

Sample Output:
11
"""
def addTwoDigits(n):
    string = str(n)
    result = int(string[0]) + int(string[1])
    return result



print(addTwoDigits(29))

