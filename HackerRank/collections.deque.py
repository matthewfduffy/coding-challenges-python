"""
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.


[TASK]
Perform append, pop, popleft and appendleft methods on an empty deque d

[Input Format]
The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

[Output Format]
Print the space separated elements of deque d.

[Sample Input]
6
append 1
append 2
append 3
appendleft 4
pop
popleft

[Sample Output]
1 2
"""
from collections import deque

n = int(input())
dq = deque()
 

for _ in range(n):
    input_str = input().split()
    action = input_str[0]

    if len(input_str) > 1:
        val = int(input_str[-1])

    match action:
        case "append":
            dq.append(val)
        case "appendleft":
            dq.appendleft(val)
        case "pop":
            dq.pop()
        case "popleft":
            dq.popleft()

print(*dq)