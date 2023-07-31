# Returns smaller lists by decomposing a list by a specified size

def decomp(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


# for testing:
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
print(decomp(a, 3))
# [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L']]