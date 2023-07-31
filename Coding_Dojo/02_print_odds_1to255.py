# 2. Print all odd integers from 1 to 255

# Option 1 - For Loop:
for i in range(1, 256):
    if i % 2 != 0:
        print(i)


# Option 2 - While Loop:
count = 1
while count <= 255:
    print(count)
    count += 2


# Option 3 - Recursively:
def odds_1_to_255(n=1):
    if n == 255:
        return n
    else: 
        print(n)
        return odds_1_to_255(n + 2)

print(odds_1_to_255())