# 1.1 Создайте программу для игры с конфетами человек против человека.
# + не умный бот
# a) Добавьте игру против бота


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
# b = 1
while a > 0:
    if b == 1:
        f = True
        while f == True:
            print('max =',max, '            ','a =',a)
            print(b , 'player write a number ')
            c = int(input())
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
                # f = False
    else:            
        print('max =',max, '            ','a =',a)
        if a > max:
            c = random.randint(1, max)
        if a < max:
            c = random.randint(1, a)
        print('2 player has made a move')
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
