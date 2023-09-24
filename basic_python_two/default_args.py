def sum(num1, num2, num3=0): # kono kisu opsonal hisabe rhakte  =0 dite pari
    result = num1 + num2+num3
    return result

total = sum(99, 11)
print('total: ', total)

#arge 
def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(22, 44, 55, 66, 77)
print('all sum:', total)
