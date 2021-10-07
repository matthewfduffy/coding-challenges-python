"""
    Practice > Python > Basic Data Types > List Comprehensions

    You are given three integers x, y, & z representing the dimensions of a cuboid along with an integer N. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to N. 

[Example]
All permutations of [i,j,k] are:

Print an array of the elements that do not sum to n = 3

[Input Format]
    Four integers x, y, z and n each on a separate line.

[Constraints]
    Print the list in lexicographic increasing order.

[Sample Input 0]

    1
    1
    1
    2

[Sample Output 0]

    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

[Explanation 0]

Each variable x,y,z will have values of 0 or 1 . All permutations of lists in the form .
Remove all arrays that sum to

to leave only the valid permutations.

[Sample Input 1]
    2
    2
    2
    2

[Sample Output 1]

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

"""



x = 2
y = 2
z = 2
n = 2

# Prints all lists without constraints
# my_list = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             my_list.append([i, j, k])

# print(my_list)

my_list = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if (i + j + k) != n:
                my_list.append([i, j, k])

print(my_list)