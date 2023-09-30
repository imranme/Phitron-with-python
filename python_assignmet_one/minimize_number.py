N = int(input())
sequence = list(map(int, input().split()))

count = {}

answer = 0

for num in sequence:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1


for num, freq in count.items():
    if freq > num:
        answer -= (freq - num)
    else:
        answer += freq

print(answer)
