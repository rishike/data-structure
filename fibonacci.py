

def fibonaaci_iterative(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a


def fibonacci_recursive(n, memo={}):

    if (n in memo.keys()):
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

def fib(n):
    if n <= 2:
        return 1
    i=1
    while (i<n):
        return fib(n-1) + fib(n-2)

# print(fib(10))
# print(fibonaaci_iterative(100))
print(fibonacci_recursive(100))