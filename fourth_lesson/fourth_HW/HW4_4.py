# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

print()
import random
k = 10
print(k)

list = []
for i in range(k+1):
    list.append(i)
# print(list)
print('----------')

list2 = (random.sample(list, k))
# print(list2)
# print('===========')

list3 = list[::-1]
# print('list3 = ',list3)

list4 = [' - ', ' + ']
l4 = random.randint(0,1)

# print()
stri = ''
for i in range( k):
    list_str = str(list2[i])
    pow_str = str(list3[i])
    l4 = random.randint(0,1)
    zn = list4[l4]
    stri = stri + list_str + 'x**'+ pow_str + zn

# print(stri)

stri2 = stri + str(random.randint(1, k)) + ' = 0'

print(stri2)

with open('HW4_4.txt', 'w') as file:
    file.write(stri2 + '\n')


print()