# candies
#   https://app.codesignal.com/arcade/code-arcade/intro-gates/DdNKFA3XCX6XN7bNz

"""
n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

Sample Input:
    n = 3
    m = 10

Sample Output:
    9 # Each child will eat 3 pieces
"""
def candies(n, m):
    return (m // n) * n

print(candies(3, 10))