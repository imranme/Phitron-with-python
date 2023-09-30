# def split_balanced_string(S):
#     count = 0
#     result = []

#     count_L = 0
#     count_R = 0

#     for char in S:
#         if char == 'L':
#             count_L += 1
#         else:
#             count_R += 1
        
#         if count_L == count_R:
#             count += 1
#             result.append(S[:count_L + count_R])
#             S = S[count_L + count_R:]

#     return count, result

# S = input()

# count, result = split_balanced_string(S)
# print(count)
# for balanced_str in result:
#     print(balanced_str)


# def count_balance_strings(S):
#     balance_count = 0
#     count_L = 0
#     count_R = 0

#     for char in S:
#         if char == 'L':
#             count_L += 1
#         else:
#             count_R += 1

#         if count_L == count_R:
#             balance_count += 1
#             count_L = 0
#             count_R = 0

#     return balance_count, result

# S = input()

# result = count_balance_strings(S)
# print(result)
# for balanced_str in result:
#    print(balanced_str)

# count, result = count_balance_strings(S)
# print(result)
# for balanced_str in result:
#     print(balanced_str)

def count_balance_strings(S):
    balance_count = 0
    count_L = 0
    count_R = 0
    result = []

    for char in S:
        if char == 'L':
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            balance_count += 1
            result.append(S[:count_L + count_R])
            S = S[count_L + count_R:]
            count_L = 0
            count_R = 0

    return balance_count, result

S = input()

count, result = count_balance_strings(S)
print(count)
for balanced_str in result:
    print(balanced_str)


