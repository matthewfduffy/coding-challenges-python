from collections import defaultdict

group_size = input().split()
# d = defaultdict(lambda: -1)
group_a = []
group_b = []


for _ in range(int(group_size[0])):
    group_a.append(input())

for _ in range(int(group_size[1])):
    group_b.append(input())

counter = len(group_a) if (len(group_a) <= len(group_b)) else len(group_b)

print("Counter size is " + str(counter))
for _ in range(counter):
    if group_b[_] in group_a:
        print(group_a.index(group_b[_]), end=" ")
# print(group_a)
# print(group_b)