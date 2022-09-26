# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('')
print('Write X coordinate'); 
a = int(input())
print('Write Y coordinate'); 
b = int(input())
print('-------------')
if (a > 0 and b > 0):
    print('Coordinae (', a,':',b, ') of point included 1 quarter')
elif (a > 0 and b < 0):
    print('Coordinae (', a,':',b, ') of point included 2 quarter')
elif (a < 0 and b < 0):
    print('Coordinae (', a,':',b, ') of point included 3 quarter')
elif (a < 0 and b > 0):
    print('Coordinae (', a,':',b, ') of point included 4 quarter')
elif a == 0:
    print('Coordinae (', a,':',b, ') of point is on the axis X')
elif b == 0:
    print('Coordinae (', a,':',b, ') of point is on the axis Y')
else:
    print()
print('-------------')

print('')