# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в 
# файле file.txt в одной строке одно число.

print('')
print('Write a namber'); 
n = int(input())

print('-----------')
with open('D:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/second_lesson/second_HW/file.txt','r') as file:
    a = int(file.readline())
    b = int(file.readline(2))

print('a =', a)
print('b =', b)

print('-------')
list = []
sum = 0
for i in range(-n, n+1):
    list.append(i)

print(list)
# print('sum =', sum)
print('-----------')

print(list[a])
print(list[b])
print('------------')
p = list[a] * list[b]

print(p)

print()