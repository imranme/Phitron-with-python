def fibonacci_of(n, memo={}):
    if n in memo:
        return memo[n]
    if n in {0, 1}:
        return n
    result = fibonacci_of(n-1, memo) + fibonacci_of(n-2, memo)
    memo[n] = result
    return result

n = int(input())

for i in range(n):
    print(fibonacci_of(i), end=" ")
