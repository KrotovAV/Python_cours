# 3.1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print()
import random
from functools import reduce
from itertools import starmap
n = random.randint(1, 10)
print('n = ', n)

# i = 0
# list = []
# for i in range(n):
#     list.append(random.randint(1, 10))
list_n = [random.randint(1, 10) for _ in range(n)]

print(list_n)
print('----------')

# sum1 = 0
# for a in range(len(list_n)):
#     if a%2 == 0:
#         sum1 = sum1 + list_n[a]

# list_nn = list(starmap(lambda x, y: y if x %2 != 0 else y -y, enumerate(list_n, 1))) 
# sum = reduce(lambda sum, x: sum +x, list_nn)

list_nn = list(starmap(lambda x, y: y if x %2 != 0 else y -y, enumerate(list_n, 1))) 
sum = reduce(lambda sum, x: sum +x, list_nn)

# print('sum1 = ' ,sum1)
print('sum = ' ,sum)
