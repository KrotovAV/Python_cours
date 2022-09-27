#4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('')
print('Write a namber of quarter'); 
a = int(input())

print('-------------')
if (a < 1 or a > 4):
    print('!!!ERROR !!! Write a namber from 1 to 4')
elif a == 1: #(a > 0 and b > 0)
    print('X coordinae > 0, Y coordinae > 0')
elif a == 2: #(a > 0 and b < 0)
    print('X coordinae > 0, Y coordinae < 0')
elif a== 3: #(a < 0 and b < 0)
    print('X coordinae < 0, Y coordinae < 0')
elif a==4: #(a < 0 and b > 0)
    print('X coordinae < 0, Y coordinae > 0')
else:
    print()

print('')