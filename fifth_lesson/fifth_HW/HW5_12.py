# 1.1 Создайте программу для игры с конфетами человек против человека.
# + бот поумней
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


import random
print()
print('Start game')
print()
b = random.randint(1, 2)
print('Write a namber'); 
a = int(input())
print('Write max nanber to subtract'); 
max = int(input())

# a = 55
# print('a =', a)

# min = 23

while a > 0:
    f = True
    print('max =',max, '            ','a =',a)
    if b == 1:
        print('1 player write a number ')
        c = int(input())
    else:
        if a > max:
            r = random.randint(3, 4)
            print('r = ', r)
            if r == 3:
                c = max
            else:
                c = random.randint(1, max)
        if a < max:
            c = a - 1
        if c == 0:
            c  = 1
        print('2 player has made a move')

    while f == True:
        
        if c > max:
            print()
            print('Namber is over max ',max)
            print('write a namber again')
            print()
            f = True
        else:
            f = False
        if (a - c) < 0:
            print()
            print('Namber is over a')
            print('write a namber again')
            print()
            f = True
        else:
            f = False
         
    print(c)
    print('----------------------')
    a = a - c

    if b == 1:
        b = 2
    else:
        b = 1
    # print(b)
    # print(a)

print()
if b == 1:
    print('!!! Player 1 win. !!!')
else:
    print('!!! Player 2 win. !!!')
print()