# 3. Напишите программу, в которой пользователь 
# будет задавать две строки, программа - определять количество 
# вхождений одной строки в другой.

str1 = 'а аб аабв ааббввгг'
str2 = 'а  ааббввгг а аб ааббввгг а аб  ааббввгг а аб аабв ааббввгг'

def stringToList (str1):
    list1 = []
    ch = 0
    for i in range(len(str1)):
            if str1[i] == ' ':
                ch = ch + 1

    a = ''
    c = 0
    str1 = str1 + ' '
    # print(str1)

    for n in range(ch+1):
        for i in range(c, len(str1)):
            if str1[i] != ' ':
                a = a + str1[i]
                c = c + 1
            else:
                list1.append(a)
                c = c + 1
                a= ''
    return list1

print('')
print(str1)
print(str2)

list1 = stringToList (str1)
list2 = stringToList (str2)
# print('--------------')
# print(list1)
# print(list2)
print('--------------')

dict = {}

co = 0
for j in range(len(list1)):
    for m in range(len(list2)):
        if list1[j] == list2[m]:
            co = co + 1
    if co != 0:
        dict[list1[j]] = co
    co = 0

print(dict)

print('')
