# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0:
# Уравнение считать из файла: # 2*x² + 4*x -2 = 0 вытащить коэффициенты А, В и С.
# коэфф могут быть любые от 0 до 999999 с учетом знака ' + ' или ' - '
# результаты записать в файл

# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

print()
with open('4_21.txt') as s:
    s = s.readline()

print(s)

nambers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(nambers[2])
str = ''
for i in range(len(s)):
    if s[i] == ' ':
        # print(s[i])
        str = str + s[i]
    for n in range(len(nambers)):
        if nambers[n] == s[i]:
            if s[i-1] == '*':
                str = str
            # print(s[i])
            else:
                str = str + s[i]
    if s[i] == '-':
        str = str + s[i]

print('str= ', str)

list1 = []
k = 0
# print(len(list1))
for ch in range(len(str)):
    ss = ''
    for k in range(k, len(str)):
        # print(str[k])
        if str[k] != ' 'or str[k] == '-':
            ss = ss + str[k]
        else:
            if ss != '':
                list1.append(ss)
                ss = ''

print('list1 = ', list1)

ch = 0
for k in range(len(str)):
    if str[k] == '-':
        ch = ch + 1
# print('ch = ',ch)

list3 = []
f = 0
le = len(list1) - ch
# print('le= ', le)

for k in range(le):
    while f < len(list1):
        # print('f = ', f)
        if list1[f] == '-':
            list1[f] = list1[f] + list1[f + 1]
            # print(list1[f])
            list3.append(list1[f])
            f = f + 2
        else:
            # print(list1[f])
            list3.append(list1[f])
            f = f + 1

print('list3 = ',list3)

print('----------------')

A = int(list3[0])
B = int(list3[1])
C = int(list3[2])

# print(A)
# print(B)
# print(C)

D = B * B - 4 * A * C
print('D = ', D)

print('уравнение: ', A, '**x + ',B , '* x +', C , ' = 0 ', end=' ')

if D < 0:
    print('не имеет корней')
    x1 = None
    x2 = None
if D == 0:
    print('имеет один корень х')
    x1 = -1 *(B/(2*A))
    print('x = ', x1)
    x2 = None
if D > 0:
    print('имеет два корня х1 и х2')
    x1 = ((-1 * B) + D ** (0.5))/(2*A)
    print('x1 = ', x1)
    x2 = ((-1 * B) - D ** (0.5))/(2*A)
    print('x2 = ', x2)

with open('4_22.txt', 'w') as file:
    file.write(repr(x1) + '\n')
    file.write(repr(x2) + '\n')

print()