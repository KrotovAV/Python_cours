import model
import view

tel = [['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки'], 
        ['001', 'Сергей', 'Сергеевич', 'Сергеев', '24585822', 'сосед'], 
        ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий'],
        ['003', 'Стас', 'Стасович', 'Стасов', '25698742', 'дача'],
        ['004','Ольга Сергей', 'Олеговна', 'Олегович', '74854925', 'парикмахер']]
# [[' 1.№ ', ' 2.Имя  ', ' 3.Отчество ', ' 4.Фамилия ', ' 5.№тел.  ', ' 6.Заметки ', '\n'], [' 001 ', ' Серей  ', ' Сергеевич  ', ' Сергеев   ', ' 24585822 ', ' сосед     ', '\n'], [' 002 ', ' Иванна ', ' Ивановна   ', ' Иванова   ', ' 25896587 ', ' рабочий   ', '\n'],
# ['003', 'f', 'bfbfb', 'bdsba', 'vadsvad', 'dv', '\n']]
# ph_book_list = tel
# val = '3'
# val_search = 'ов'

print()
def search(ph_book_list, val, val_search):
    j = int(val) - 1
    # res_list = []
    res_list = [ph_book_list[0]]
    ph_book_list[0][-1] = ph_book_list[0][-1] + '\n'
    if val == '7':
        for i in range(1, len(ph_book_list)):
            for j in range(len(ph_book_list[i])):
                if val_search in ph_book_list[i][j]:
                    print('y=',ph_book_list[i][j])
                    res_list.append(ph_book_list[i])
                    ph_book_list[i][-1] = ph_book_list[i][-1] + '\n'
                    break
    else:
        for i in range(1, len(ph_book_list)):
            # print(ph_book_list[i])
            if val_search in ph_book_list[i][j]:
                print('x=',ph_book_list[i][j])
                res_list.append(ph_book_list[i])
                ph_book_list[i][-1] = ph_book_list[i][-1] + '\n'
    if len(res_list) == 1:
        se = res_list.append([val_search,'  -   N O T   F O U N D   '])# (['--','----','----','--NOT--','-FOUND--',' '])
    se = (''.join(list(map(lambda x: '|'.join(x), res_list))))
    se = se.replace('\n|','')
    return se

def show_all(list_list):
    # print('1=',list_list)
    list_b = []
    for j in range(len(list_list[0])):
        list_b.append(max([len(list_list[i][j]) for i in range(len(list_list)-1)]))
    # print('2=',list_list)
    for i in range(len(list_list)):
        for j in range(len(list_list[i])):
            if list_b[j] != len(list_list[i][j]):
                list_list[i][j] = list_list[i][j]+ ' '*(list_b[j] -len(list_list[i][j]))
        if list_list[i][-1] != '\n':
            list_list[i].append('\n')
    text_str = ''.join(list(map(lambda x: '|'.join(x), list_list)))
    # print('3=',list_list)
    return text_str

def my_split(text):
    list_text = text.splitlines()
    for i in range(len(list_text)):
        list_text[i] = list_text[i].split('|')
    return list_text

search_string = search(tel, '7', 'ж')

search_string = my_split(search_string)
print(show_all(search_string))




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
 