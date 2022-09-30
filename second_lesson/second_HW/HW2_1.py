# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('')
print('Write a namber'); 
n = float(input())

print('-------')

while 0 < n%1 < 1:
    n = n * 10

s = 0
while n != 0:
    a = int(n % 10)
    n = int((n - a)/10) 
    s = s + a
    # print(a, ', ', n, ', ', s)

# print('-------')

print(s)