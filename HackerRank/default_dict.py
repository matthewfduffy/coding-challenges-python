"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

Example:
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

#('python', ['awesome', 'language'])
#('something-else', ['not relevant'])
"""
"""
In this challenge, you are given 2 integers, n and m. 
There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. 
If it does not appear, print -1.

Example:
Group A contains 'a', 'b', 'a'
Group B contains 'a', 'c'
For the first word in grou B, 'a', it appears at positions 1 and 3 in Group A.
The second word, 'c', does not appear in group A, so print -1

[Sample Input]:
5 2     # group A size n = 5, group B size m = 2
a
a
b
a
b
a   # Group B
b

[Sample Output]:
1 2 4 
3 5
"""

from collections import defaultdict

group_a, group_b = map(int, input().split())
d = defaultdict(list)

for letter in range(1, group_a + 1):
    a = input()
    d[a].append(letter)

for letter in range(group_b):
    b = input()
    if d[b]:
        print(*d[b])
    else:
        print("-1")



