# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# o Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


print('')
print('Write a nam'); 
n = int(input())
print('---------------------')
dict = {}
for i in range(1, n):
    dict[i] = (i*3 + 1)
print(dict)
print('')