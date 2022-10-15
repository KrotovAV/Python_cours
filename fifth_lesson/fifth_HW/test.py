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
print(a_list)

arch_list = []
co = 0
for i in range(len(a_list)-1):
    if a_list[i] != a_list[i+1]:
        print('xxxx')
        arch_list.append(a_list[i])
    if a_list[i] == a_list[i+1]:
        co = co +1
    arch_list.append(co)
    co = 0
print(arch_list)
# for i in range(len(a)):
#     print(a[i])
#     rch_dict[i] = 

# key = str(list(pl_fi.keys())[list(pl_fi.values()).index(c)])
#     if a == 1:
#         pl_fi[key] = 'x'

# with open('HW5_32.txt', 'w') as file:
#     file.write(new_eq + '\n')



# with open('HW5_32.txt') as b:
#     b = b.readline()

print()