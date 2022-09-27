# 5 Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('')

print('-------------')

def write(a, b):
    print('Write ', b,' coordinate of ', a,' point')
    c = int(input())
    globals()[a + b] = c
    return a+b, c

write('A', 'X')
write('A', 'Y')
write('B', 'X')
write('B', 'Y')
print('---------------')
print('Coordinate of A point (', AX,';',AY,')')
print('Coordinate of B point (', BX,';',BY,')')

print('---------------')

distance = ((AX - BX)**2 + (AY - BY)**2)**0.5
print('Distance =', round(distance,2))
print()