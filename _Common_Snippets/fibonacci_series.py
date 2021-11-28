x = 5

fact = [lambda x : x if x <= 1 else fib(x-1) + fib(x-2)]
print(fact)