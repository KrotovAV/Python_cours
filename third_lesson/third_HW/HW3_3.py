# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, 
# у целых чисел дробной части нет их в расчет не берем

# *Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print()
import random

n = random.randint(3, 10)
print('n = ', n)

list = []
for i in range(n):
    list.append(round(random.uniform(0, 10), 2))
print('list1 = ', list)
print('----------')

# list[2] = random.randint(3, 10)
# print(list)
# print('----------')

list2 = []
for i in range(n):
    list2.append(round(list[i] - int(list[i]), 2))
    
# print('list2 = ',list2)
# print('----------')

min = list2[0]
max = list2[0]

for j in range(len(list2)):
    if list2[j] != int(list2[j]):
        if list2[j] > max:
            max = list2[j]
        if list2[j] < min:
            min = list2[j]

# print('max =', max)
# print('min =', min)

# print('----------')
difference = round((max - min), 2)
print('difference =', difference)

print()