# Checks for duplicates in a list

# Option 1
def dupe_check(x):
    return len(x) != len(set(x))


lst_one = [1, 2, 3, 4, 5]
lst_two = [1, 2, 3, 4, 4, 5, 6]

print(dupe_check(lst_one))  # False (no duplicates)
print(dupe_check(lst_two))  # True  (has duplicates)
