# 1. Дан список чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5] , [2, 3, 4, 6] или [6, 7] и т.д.

import random
print()

list1 = [x for x in range(1,10)]
# print(list1)
random.shuffle(list1)

# print('--------------')
print(list1)

main_list = []
for i in range(len(list1) - 1):
    mini_list = [list1[i]]
    for j in range(i, len(list1)-1):
        if list1[j] < list1[j+1]:
            mini_list.append(list1[j+1])
        else:
            break
    main_list.append(mini_list)
# print(main_list)

final_main_list = []
for i in range(len(main_list)):
    if len(main_list[i]) > 1:
        final_main_list.append(main_list[i])
print(final_main_list)
print()