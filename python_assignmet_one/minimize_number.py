# N = int(input())
# sequence = list(map(int, input().split()))

# count = {}

# answer = 0

# for num in sequence:
#     if num not in count:
#         count[num] += 1
#     else:
#         count[num] = 1


# for num, freq in count.items():
#     if freq > num:
#         answer += (freq - num)
#     elif freq < num:
#         answer += freq

# print(answer)


N = int(input())
sequence = list(map(int, input().split()))

count = {}

for num in sequence:
    count[num] = 0

for num in sequence:
    count[num] += 1

answer = 0

for num, freq in count.items():
    if freq > num:
        answer += freq - num
    elif freq < num:
        answer += freq

print(answer)


def do_a_lot(*args):
    print(args)



def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))