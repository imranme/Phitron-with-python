N = int(input())
arr = list(map(int, input().split()))
min_val, max_val = min(arr), max(arr)
min_index, max_index = arr.index(min_val), arr.index(max_val)
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(*arr)



