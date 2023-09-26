#list use --> []
# tuple use --> ()
#set -->{}
# set: unique items collection 

num = [12, 23, 45,56,34, 56,45]
# print(num)
num_set = set(num)
# print(num_set)
num_set.add(100)
print(num_set)

print(sorted(num_set))

num_set.remove(12)
print(num_set)

for item in num_set:
    print(item)
if 5 in num_set:
    print('5 exists')
elif 23 in num_set:
    print('exitst')


