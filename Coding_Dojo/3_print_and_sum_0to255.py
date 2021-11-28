# Print integers from 0 to 255, and with each integer print the sum so far.

sum = 0
for i in range(0, 256):
    sum += i
    print("The current integer is: ", i)
    print("\tThe current sum is: ", sum)