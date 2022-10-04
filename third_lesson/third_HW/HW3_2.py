# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print()
import random
n = random.randint(1, 10)
print('n = ', n)

list = []
for i in range(n):
    list.append(random.randint(1, 10))
print(list)
print('----------')

list2 = []

if n%2 == 0:
    len_list = int(n/2)
else:
    len_list = int(n/2 + 1)

for a in range(len_list):
    list2.append(list[a]*list[n-1-a])

print(list2)

print()