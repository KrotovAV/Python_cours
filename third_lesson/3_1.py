#1 Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

print('')
# print('Write a namber for find'); 
# a = str(input())
a = str(3)

list = ['5hh33', 'a', 'u5v335', 'g1d', '45vd', '9h']

print('')
print(list)
print(a)

print('--------')
count = 0
for i in list:
    b = i
    # print('--')
    for k in b:
        # print(k)
        if a == k:
            count = count + 1
    if count != 0:
        print('namber',a ,'exist in "', b, '" ', count, 'times')
    count = 0

print('--------')

print('')