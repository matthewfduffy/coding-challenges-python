"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Rahu earned.

[Input Format]:
    The first line contains X, the number of shoes.
    The second line contains the space separated list of all the shoe sizes in the shop.
    The third line contains N, the number of customers.
    The next N lines contain the space separated values of the shoe size desired by the customer and Xi, the price of the shoe.

[Sample Input Format]:
    10
    2 3 4 5 6 8 7 6 5 18
    6 
    6 55
    6 45
    6 55
    4 40
    18 60
    10 50

[Sample Output]:
    200

[Explanation]:
    Customer 1: Size 6 shoe for $55
    Customer 2: Size 6 shoe for $45
    Customer 3: No purchase; No more size 6 shoe
    Customer 4: Size 4 shoe for $40
    Customer 5: Size 18 shoe for $40
    Customer 6: Size 10 shoe not available
"""

# Option 1: without collections.Counter()

num_shoes = int(input())
shoe_sizes = input().split()
num_customers = int(input())
total_sold = 0

for _ in range(num_customers):
    customer_order = input().split()
    if customer_order[0] in shoe_sizes:
        total_sold += int(customer_order[1])
        shoe_sizes.remove(customer_order[0])
        
print(total_sold)



# Option 2: WITH collections.Counter()

from collections import Counter

num_shoes = int(input())
shoe_sizes = [int(_) for _ in input().split()]
size_counter = Counter(shoe_sizes)
num_customers = int(input())
total_sold = 0

for _ in range(num_customers):
    order = input().split()
    size, price = int(order[0]), int(order[1])
    if size_counter[size] > 0:
        total_sold += price
        size_counter[size] -= 1

print(total_sold)