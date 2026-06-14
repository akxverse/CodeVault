# Recursion in Python

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Sequence:")

for i in range(8):
    print(fibonacci(i), end=" ")