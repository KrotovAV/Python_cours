# 3. Напишите программу, в которой пользователь 
# будет задавать две строки, программа - определять количество 
# вхождений одной строки в другой.

from re import I


str_sub= 'а аб аабв ааббввгг'
str_src = 'а аб аабв ааббввгг а  ааббввгг а аб ааббввгг а аб  ааббввгг а аб аабв ааббввгг'
# print(type(str1))
# print(type(str2))

def count_substring(sourse, sub):
    len_sub = len(sub)
    len_sourse = len(sourse)
    i = 0
    for iend in range(len_sub, len_sourse + 1):
        if sourse[iend - len_sub: iend] == sub:
            i+= 1
    return i

print(f'Число вхождений строки "{str_sub}" в строку  "{str_src}" =', count_substring(str_src, str_sub))
print(f'Проверка с помощью str.count()) -> {str_src.count(str_sub)}')

stroka= 'abcdefg'
print(stroka[1:3])

