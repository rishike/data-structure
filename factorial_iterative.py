
def factorial2(n, memo={}):
    if (n in memo.keys()):
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = n * factorial2(n-1, memo)
    return memo[n]

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)

print(factorial2(4))

# def factorial_iterative_while(n):
#     result = 1
#     while n >= 1:
#         result *= n
#         n -= 1
#     return result
# 
# 
# assert factorial_iterative_while(4) == 24
# assert factorial_iterative_while(6) == 720