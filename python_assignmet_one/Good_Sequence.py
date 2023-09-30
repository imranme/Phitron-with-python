# N = int(input())
# sequence = list(map(int, input().split()))

# count = {}
# for num in sequence:
#     count[num] = count.get(num, 0) + 1

# removals = 0
# for num, freq in count.items():
#     removals += max(0, freq - num)

# print(removals)

# Read input
N = int(input())
sequence = list(map(int, input().split()))

# Create a dictionary to count the occurrences of each number
count = {}

# Initialize the removal count to 0
removals = 0

# Iterate through the sequence and count occurrences
for num in sequence:
    # If the number is not in the dictionary, add it with a count of 1
    if num not in count:
        count[num] = 1
    else:
        # If the number is already in the dictionary, increment its count
        count[num] += 1

    # If the count for the current number exceeds the number itself, it's a candidate for removal
    while count[num] > num:
        # Increment removal count
        removals += 1
        # Decrement the count of the current number
        count[num] -= 1

# Print the minimum number of elements to remove
print(removals)


