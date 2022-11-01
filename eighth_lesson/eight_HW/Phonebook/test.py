
path = 'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'
with open(path,'r', encoding='utf8') as text:
    text = text.read()
# print(text)

list_text = text.splitlines()
for i in range(len(list_text)):
    list_text[i] = list_text[i].split('|')

print((len(list_text)))
# print(i)
# print(j)

list_b = []
for j in range(6-1):
    list_b.append(max([len(list_text[i][j]) for i in range(len(list_text)-1)]))
# print(list_b)

for i in range(len(list_text)):
    for j in range(6-1):
        list_text[i][j] = ' ' + list_text[i][j]+ ' '*(list_b[j]+1 -len(list_text[i][j]))
    list_text[i].append('\n')
# print('----------------')

text_str = ''.join(list(map(lambda x: '|'.join(x), list_text)))
print(text_str)

print('----------------')
# №|Name|Second Name|Last name|Fone namber|Note
# №|Имя|отчество|Фамилия|Номер телефона|Заметки


# data = input().split() # о умолчанию символ разделитель пробел
# data = input().split(',') # символ разделитель запятая
# data = list(map(int, input().split()))
# print(data)

# print(list_text[2][1])

# >>> elements = ['слон', 'кот', 'лошадь', 'змея', 'рыба']
# >>> if 'кот' in elements:
# 	print('meow')	

# with open('4_12.txt', 'w') as file:
#     file.write(min_str + '\n')
#     file.write(max_str + '\n')


# with open('HW5_33.txt', 'w') as file:
#     file.write(arch_str + '\n')

# with open('HW5_32.txt', 'w') as file:
#     file.write(arch_key_str + '\n')

# print('-----------------------')

# with open('HW5_32.txt') as b:
#     b = b.readline()

# with open('4_11.txt', 'w') as file:
#     file.write(strin)

# with open('4_11.txt') as s:
#     s = s.readline() 
 