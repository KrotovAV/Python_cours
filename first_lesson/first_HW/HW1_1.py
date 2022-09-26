# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print('')
print('Write a namber from 1 to 7'); 
a = int(input())
print('-------------')

if (a < 1 or a > 7):
    print('namber is not from 1 to 7')
    print('')
    quit()

if (a > 0 and a > 5 and a < 8):
    print(list[a+1],'it is a day off')
else:
    print(list[a+1], 'it is a work day')

print('')