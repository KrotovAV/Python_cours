# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

print()
arch_dict = {}
with open('HW5_31.txt') as a:
    a = a.readline() 
print(a)
a_list = []
for i in range(len(a)):
    # print(a[i])
    a_list.append(a[i])

a_list.append('')
# print('a_list =', a_list)

arch_list = []
co = 0
for i in range(len(a_list)-1):
    if a_list[i] != a_list[i+1]:
        arch_list.append(a_list[i])
     
# print('arch_list =',arch_list)

key_list = []
co = 0
for i in range(len(arch_list)):
    # print(arch_list[i])
    key_list.append(arch_list[i])
    for j in range(len(a_list)-1):
        if arch_list[i] == a_list[j]:
            co = co + 1
    key_list.append(str(co))
    co = 0
# print('key_list =', key_list)

arch_key_str = ''
for i in range(len(key_list)):
    arch_key_str = arch_key_str + key_list[i]
# print('arch_key_str =', arch_key_str)


with open('HW5_32.txt', 'w') as file:
    file.write(arch_key_str + '\n')

print('-----------------------')

with open('HW5_32.txt') as b:
    b = b.readline()
# print(b)

arch_key_list = []
for i in range(len(arch_key_str)):
    # print(a[i])
    arch_key_list.append(arch_key_str[i])
# print(arch_key_list)

n_arch_list = []
for i in range(0, len(arch_key_list), 2):
    a = 0
    while a < int(arch_key_list[i+1]):
        n_arch_list.append(arch_key_list[i])
        a = a +1

# print(n_arch_list)
# print()

arch_str = ''
for i in range(len(n_arch_list)):
    arch_str = arch_str + n_arch_list[i]
print(arch_str)

print()

with open('HW5_33.txt', 'w') as file:
    file.write(arch_str + '\n')