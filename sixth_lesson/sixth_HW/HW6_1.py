# 4.1 Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# 45 658 4527 24 512 548 9654 12 2 2 45 

print()
import random
n = random.randint(1, 10)
print('n = ', n)

# listr = []
# for i in range(n):
#     list.append(random.randint(1, 999))

list_r = [random.randint(1,999) for _ in range(n)]
print(list_r)

strin = ''
for i in range(n):
    strin = strin + ' ' + str(list_r[i])

strin = strin.replace(' ', '', 1) 

# print(strin)
print('----------')

with open('4_11.txt', 'w') as file:
    file.write(strin)

with open('4_11.txt') as s:
    s = s.readline() 
# print(s)
s_str = s.split(' ',)
# print(s_str)

# for i in range(len(s_str)):
#     s_str[i] = int(s_str[i])
s_str = list(map(int, s_str))

# print(s_str)

# max_n = s_str[0]
# min_n = s_str[0]
# for i in range(len(s_str)):
#     if s_str[i] > max_n:
#         max_n = s_str[i]
#     if s_str[i] < min_n:
#         min-N = s_str[i]

min_n = min(s_str);
max_n = max(s_str);

print('min = ', min_n,', ', 'max = ', max_n)

# min_str = str(min_n)
# max_str = str(max_n)

# with open('4_12.txt', 'w') as file:
#     file.write(min_str + '\n')
#     file.write(max_str + '\n')

with open('4_12.txt', 'w') as file:
    file.write(str(min_n) + '\n')
    file.write(str(max_n) + '\n')

print()