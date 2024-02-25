'''

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

[Input Format]

A single line containing a string S

[Constraints]
0 < len(s) < 1000

[Output Format]

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 

[Sample Input]
qA2

[Sample Output]
True
True
True
True
True
'''

def string_validators(s):
    tracker = False
    
    for letter in s:
        if letter.isalnum():
            tracker = True
    
    print(tracker)


    tracker = False
    for letter in s:
        if letter.isalpha():
            tracker = True
    
    print(tracker)
    
    tracker = False
    for letter in s:
        if letter.isdigit():
            tracker = True

    print(tracker)

    tracker = False
    for letter in s:
        if letter.islower():
            tracker = True

    print(tracker)
    
    tracker = False
    for letter in s:
        if letter.isupper():
            tracker = True

    print(tracker)

    




string_validators("qA2")