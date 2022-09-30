# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# o Для N = 5: 1, -3, 9, -27, 81


print('')
print('Write a nam'); 
a = int(input())
print('---------------------')
m = [1]
for i in range(0, a):
    m.append(m[i]*3)
    if(i%2 != 0):
        m[i] = - m[i]
    print(m[i], ',', end='')
print('')
print('')