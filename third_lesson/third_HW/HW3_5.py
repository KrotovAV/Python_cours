# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

print('')
print('Write a namber'); 
n = int(input())
# n = 4

print('')
print('n =', n)
print('---')

def fibo(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    if a > 2:
        return fibo(a - 1) + fibo(a - 2)
    
list = []
for i in range(-n, n+1):
    f = fibo(abs(i))
    if i < 0 and i%2 == 0:
        f = -f
    list.append(f)

print(list)
print()