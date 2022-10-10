# 3 Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

print()
str = '47756688399943'
print(str)
print('--------------')
nambers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list = []
for i in range(len(str)):
    list.append(str[i])

# print(list)

list2 = []
co= 0
com = 1
for j in range(len(nambers)):
    co = 0
    for k in range(len(list)):
        if nambers[j] == list[k]:
            co = co + 1
    # print(nambers[j], co)
    if 0 < co < 2:
        # print(com, co)
        list2.append(nambers[j])

print(list2)
print()
