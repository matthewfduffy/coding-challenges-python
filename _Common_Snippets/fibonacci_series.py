# Option 1
fib = [0, 1]
[fib.append(fib[-2] + fib [-1]) for i in range(8)]
print(fib)	#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Option 2
x = 5
fact = [lambda x : x if x <= 1 else fib(x-1) + fib(x-2)]
print(fact)