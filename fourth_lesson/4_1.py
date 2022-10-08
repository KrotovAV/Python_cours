# Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# 45 658 4527 24 512 548 9654 12 2 2 45 

print() 

with open('4_11.txt') as s:
    s = s.readline() 
    print(s)
print()

s_str = s.split(' ', )
print(s_str)

for i in range(len(s_str)):
    s_str[i] = int(s_str[i])

max = s_str[0]
min = s_str[0]
for i in range(len(s_str)):
    if s_str[i] > max:
        max = s_str[i]
    if s_str[i] < min:
        min = s_str[i]

print('min = ', min,', ', 'max = ', max)

min_str = str(min)
max_str = str(max)

with open('4_12.txt', 'w') as file:
    file.write(min_str + '\n')
    file.write(max_str + '\n')

print() 
