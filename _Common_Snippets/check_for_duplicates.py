# Checks for duplicates in a list
a = [1, 2, 3, 4, 4, 5, 6]

def dupe_check(x):
    return len(x) != len(set(x))


print(dupe_check(a))

