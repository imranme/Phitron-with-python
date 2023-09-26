def power(X, N):
    result = 1
    for _ in range(N):
        result *= X
    return result

def calculate_equation_result(X, N):
    result = 0
    
    for i in range(N + 1):
        if i % 2 == 0:
            if i == 0:
                result += power(X, i) - 1
            else:
                result += power(X, i)

    return result

X, N = map(int, input().split())

S = calculate_equation_result(X, N)
print(S)


