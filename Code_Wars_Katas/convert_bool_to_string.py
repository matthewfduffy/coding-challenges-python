"""
[https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python]
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

"""


def boolean_to_string(b):
    return "True" if b == True else "False" 
    # This works only with the condition that 'valid' input is given

    # Better option:
    return string(b)