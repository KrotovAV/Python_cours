# 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# "2+2" => 4;
# "1+2*3" => 7;
# "1-2*3" => -5;


print()

str = '-5-4-1- 3+2+3 *4 +4/2+7-8'

print(str)

list = []
for i in range(len(str)):
    list.append(str[i])

ch = 0
while ch < len(list):
    if list[ch] == ' ':
        list.pop(ch)
    ch += 1
# print(list)

a = 0
list2 = []
list.append(' ')
c = 0
a = 0
while a <(len(list)-1):
    if list[a].isdigit() or list[a] == '0':
        c = 1
        i = a
        stri = list[a]
        if i < len(list)-1:
            while list[i+1].isdigit():
                stri = stri + list[i+1]
                c += 1
                i += 1
        a = a + c
        list2.append(stri)
    list2.append(list[a])
    a += 1

if list2[0] == '+' or list2[0] == '-':
    list2.insert(0,'0')


list2.pop()

# print(list2)
print('----------------------------')

l = len(list2)-2
n = 0
while n < l - 2:
    if list2[n+1] == '*':
        list2[n] = int(list2[n])*int(list2[n+2])
        list2.pop(n+1)
        list2.pop(n+1)
        n = 0
        l =  l - 2
    else:
        n = n + 2
# print(list2)

l = len(list2)-2
n = 0
while n < l - 2:
    if list2[n+1] == '/':
        list2[n] = int(list2[n])/int(list2[n+2])
        list2.pop(n+1)
        list2.pop(n+1)
        l = l- 2
        n = 0
    else:
        n = n + 2
# print(list2)

l = len(list2)-2
n = 0
while n < l - 2:
    if list2[n+1] == '+':
        list2[n] = int(list2[n])+int(list2[n+2])
        list2.pop(n+1)
        list2.pop(n+1)
        l =  l - 2
        n = 0
    else:
        n = n + 2
# print(list2)

l = len(list2)-2
n = 0
while n < l - 2:
    if list2[n+1] == '-':
        list2[n] = int(list2[n])-int(list2[n+2])
        list2.pop(n+1)
        list2.pop(n+1)
        l =  l - 2
        n = 0
    else:
        n = n + 2

# print(list2)

res = int(list2[0])-int(list2[2])

print(res)








print()