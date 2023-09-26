# lst = []
# n= int(input("enter: "))

# for i in range(0, n):
#     ele = int(input())
#     lst.append(ele)

# print(lst[::-1])

def print_digits_reverse(num):
    num_str = str(num)  
    reversed_digits = num_str[::-1]  
    print(" ".join(reversed_digits))  
T = int(input())

for _ in range(T):
    N = int(input()) 
    print_digits_reverse(N) 
