# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


print('')
print('Write a namber'); 
n = int(input())
# n = 73
print('')
print('namber in decimal =', n)

result = []
res = ''
while n != 0:
    b = int(n/2)
    c = n%2
    n = b
    result.append(str(c))

# print(result)

vrem = ''
b = len(result)

for i in range(len(result)):
    if i < int(b/2):
        vrem = result[b-1-i]
        result[b-1-i] = result[i]
        result[i] = vrem

print('-----')
# print(result)
namber10 = 0

for i in range(len(result)):
    namber10 = namber10*10 + int(result[i])
print('namber in binary = ', namber10)
print()