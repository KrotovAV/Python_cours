# 1. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

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
b = 1
while a > 0:
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
