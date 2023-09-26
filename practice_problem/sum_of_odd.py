def sum_of_odd(x,y):
    if x>y:
        x,y = y,x

    odd_sum =0

    for num in range(x+1,y):
        if num % 2 != 0:
            odd_sum += num
    
    return odd_sum 

T = int(input())

results = []

for _ in range(T):
    X, Y = map(int, input().split())
    result = sum_of_odd(X, Y)
    results.append(result)

for result in (results):
    print(result)
    

