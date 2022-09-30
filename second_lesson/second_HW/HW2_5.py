# 5 Реализуйте алгоритм перемешивания списка.

import random
print('')
list = ['a', 'ab', 'cg', '35k', 'df7', '1f5', 'fgr', 'rty', 'bad']

print(list)
r = len(list)
new_list = list
for i in range(len(new_list)):
    a = random.randint(1,r-1)
    new_list[i] = list[a]
    # print('i = ', i, 'a = ', a)

print('-----------')
print(new_list)
print('')