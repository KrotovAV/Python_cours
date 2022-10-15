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
print('arch_key_str =', arch_key_str)


with open('HW5_32.txt', 'w') as file:
    file.write(arch_key_str + '\n')


with open('HW5_32.txt') as b:
    b = b.readline() 



# key = str(list(pl_fi.keys())[list(pl_fi.values()).index(c)])
#     if a == 1:
#         pl_fi[key] = 'x'

# with open('HW5_32.txt', 'w') as file:
#     file.write(new_eq + '\n')



# with open('HW5_32.txt') as b:
#     b = b.readline()

print()