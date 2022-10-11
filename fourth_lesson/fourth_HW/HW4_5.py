# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + 2x^2 + 20 = 0
# 17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x^1 + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


def stringToList (str1):
    list1 = []
    ch = 0
    for i in range(len(str1)):
            if str1[i] == ' ':
                ch = ch + 1

    a = ''
    c = 0
    str1 = str1 + ' '
    print(str1)

    for n in range(ch+1):
        for i in range(c, len(str1)):
            if str1[i] != ' ':
                a = a + str1[i]
                c = c + 1
            else:
                if (str1[i-1] == '+' or str1[i-1] == '-'):
                    a = a  #+ str1[i]
                    c = c + 2
                else:
                    list1.append(a)
                    c = c + 1
                    a= ''
    return list1

print()
with open('HW4_51.txt') as a:
    a = a.readline() 
with open('HW4_52.txt') as b:
    b = b.readline()
# print('------------------------------')
list_a = stringToList(a)
# print(list_a)
# print()
list_b = stringToList(b)
# print(list_b)
# print('------------------------------')

def list_to_dict(list):
    dict = {}
    for i in range(len(list)):
        if list[i][1:].isdigit():
            dict[0] = list[i]
        else:
            if len(list[i]) > 2:
                if len(list[i]) == 4:
                    dict[int(list[i][-1])] = list[i][:-3] + '1'
                    print(dict[int(list[i][-1])])
                else:
                    dict[int(list[i][-1])] = (list[i][:-3])
    return dict

dict_a = list_to_dict(list_a)
# print(dict_a)
dict_b = list_to_dict(list_b)
# print(dict_b)

def max_in_dicts(dict1, dict2):
    max1 = 0
    for key1 in dict1:
        if key1 > max1:
            max1 = key1
    # print(max1)
    max2 = 0
    for key2 in dict2:
        if key2 > max2:
            max2 = key2
    # print(max2)
    maxx = 0
    if max1 > max2:
        maxx = max1
    else:
        maxx = max2
    return maxx

max = max_in_dicts(dict_a, dict_b)
# print('max = ', max)

def fill_dict(dicti, n):
    for i in range(0, n+1):
        dicti.setdefault(i, '0')
    if dicti[i] == '':
        print(dicti[i])
        dicti[i] = '0'
    return dicti

# print('===============')

dict_an = fill_dict(dict_a, max)
print(dict_an)
dict_bn = fill_dict(dict_b, max)
print(dict_bn)

# print('------------------------------')

dict_a_add_b = {}
for i in range(max, -1, -1 ):
    dict_a_add_b[i] = (int(dict_an[i]) + int(dict_bn[i]))

# print(dict_a_add_b)
print('------------------------------')

def dict_to_equation(dict_ab):
    str_ab = ''
    for i in range(max, -1, -1 ):
        if dict_ab[i] > 0:
            dict_ab[i] = ' +' + str(dict_ab[i])
        if dict_ab[i] == 0:
            # dict_ab[i] = ''
            str_ab = str_ab
        else:
            if i > 1:
                str_ab = str_ab + str(dict_ab[i]) + 'x^' + str(i) + ' '
            if i == 1:
                str_ab = str_ab + str(dict_ab[i]) + 'x' + ' '
            if i < 1:
                str_ab = str_ab + str(dict_ab[i]) + ' = 0'
    return str_ab

new_eq = dict_to_equation(dict_a_add_b)
print(new_eq)

with open('HW4_53.txt', 'w') as file:
    file.write(new_eq + '\n')

print()
