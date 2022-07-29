"""
    Complete the solution so that it returns true if the first argument (string) passed in ends with the 2nd argument.

    Example:
    solution('abc', 'bc')   # returns true
    solution('abc', 'd')    # returns false
"""


def solution(string, ending):
    end_length = len(ending)
    if end_length == 0:
        return True
    else:
        return True if string[-end_length:] == ending else False