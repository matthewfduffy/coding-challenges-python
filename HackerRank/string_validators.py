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
    
    # Checks if s has any alphanumeric characters
    for letter in s:
        if letter.isalnum():
            tracker = True
    print(tracker)

    # Checks if s has any alphabetical characters
    tracker = False
    for letter in s:
        if letter.isalpha():
            tracker = True
    print(tracker)
    
    # Checks if s has any digits
    tracker = False
    for letter in s:
        if letter.isdigit():
            tracker = True
    print(tracker)

    # Checks if s has any lowercase letters
    tracker = False
    for letter in s:
        if letter.islower():
            tracker = True
    print(tracker)
    
    # Checks if s has any uppercase letters
    tracker = False
    for letter in s:
        if letter.isupper():
            tracker = True
    print(tracker)

    

string_validators("qA2")


# Alternate Solution
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))