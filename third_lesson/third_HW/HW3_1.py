# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print()
import random
n = random.randint(1, 10)
print('n = ', n)

# i = 0
list = []
for i in range(n):
    list.append(random.randint(1, 10))
print(list)
print('----------')

sum = 0
for a in range(len(list)):
    if a%2 == 0:
        print(list[a], end=' ')
        sum = sum + list[a]

print()
print('----------')
print('sum = ' ,sum)
# print(n%2 == 0)

print()