# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие
#  A[i] - 1 = A[i-1]. Найдите это число.

print()
import random

k = 20

nambers = []
for i in range(k):
    nambers.append(i)

# print(nambers)

ch = random.randint(0, k)
print(ch)

for i in range(len(nambers)-1):
    if nambers[i] == ch:
        nambers.pop(i)

s_nambers = ' '.join(str(x) for x in nambers)
# print(s_nambers)


with open('5_1.txt', 'w') as file:
    file.write(str(s_nambers))

print('--------------------')

with open('5_1.txt') as str:
    str = str.readline() 
print(str)

nambers2 = str.split()
# print(nambers2)

nambers3 = list(map(int, nambers2))
# print (nambers3)

a = 0
for i in range(1, len(nambers3)):
    if nambers3[i] - 1 != nambers3[i-1]:
        a = nambers3[i]

print(a)


print()