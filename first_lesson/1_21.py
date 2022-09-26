# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

print('')
print('Введите размер массива'); 
n = int(input())

nam = []

print('----------')

for i in range(n): 
    print('')
    print('Введите ', i+1, ' элемент'); 
    nam.append(int(input()))

print('----------')

print('namber are ',nam)

print('----------')

max = 0

for i in nam: 
    if i > max:
        max = i

print('Max namber is ',max)
print('')