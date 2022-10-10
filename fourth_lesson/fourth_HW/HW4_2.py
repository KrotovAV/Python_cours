# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

print('')
# print('Write a namber'); 
# n = float(input())
n = 97

# print('Write a max of natural namber'); 
# k = float(input())
k = 999

print(n)

simpl_nambers = []
co = 0
print('-------')
for a in range(1, k):
    co = 0
    for b in range(1, a+1):
        if int(a / b) == (a / b):
            co= co + 1
    if co < 3:
        simpl_nambers.append(a)

# print(simpl_nambers)
# print('------------')

for c in range(len(simpl_nambers)):
    for v in range(len(simpl_nambers)):
        if c * v == n:
           print(c, v)

print()