# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

print('')
print('Write a namber'); 
n = int(input())

print('-------')
list = []
sum = 0
for i in range(1, n+1):
    a = (1 + 1/i)**i
    list.append(a)
    sum = sum + a

print(list)
print('sum =', sum)
print()