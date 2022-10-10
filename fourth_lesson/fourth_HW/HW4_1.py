# 1 Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

print('')
# print('Write the number of decimal places (from 0.1 to 0.0000000001):'); 
# k = int(input())
k = 0.001
print(k)

# print('Write the number to round:'); 
# a = int(input())
a = 3.1415926535897932384626433832795
print(a )

cou = 0
while 1 > k > 0:
    k = k *10
    cou = cou + 1 

d = 1
print('-------')

for i in range(cou):
    d = float(d * 10)

f = (int(a * d ))/d
print(f)

print()