# Calculate the nth permutations number
import sys

sys.setrecursionlimit(15000)

memo = dict()
def fib(n):
    if n in memo: return memo[n]
    if n <=2: return 1

    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f

def fib_bad(n):
    if n <= 2: return 1
    f = fib_bad(n - 1) + fib_bad(n - 2)
    return f

number = 32
print(fib(number))
print(fib_bad(number))