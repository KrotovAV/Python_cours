import model
import view

[['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки'], ['001', 'Серей', 'Сергеевич', 'Сергеев', '24585822', 'сосед'], ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий']]

[[' 1.№ ', ' 2.Имя  ', ' 3.Отчество ', ' 4.Фамилия ', ' 5.№тел.  ', ' 6.Заметки ', '\n'], [' 001 ', ' Серей  ', ' Сергеевич  ', ' Сергеев   ', ' 24585822 ', ' сосед     ', '\n'], [' 002 ', ' Иванна ', ' Ивановна   ', ' Иванова   ', ' 25896587 ', ' рабочий   ', '\n'],
['003', 'f', 'bfbfb', 'bdsba', 'vadsvad', 'dv', '\n']]



    for i in range(len(list_list)):
        for j in range(6):
            list_list[i][j] = list_list[i][j]+ ' '*(list_b[j]+1 -len(list_list[i][j]))
            list_list[i].append('\n')
    text_str = ''.join(list(map(lambda x: '|'.join(x), list_list)))





ph_book = model.main()
print('----------------')
def add_kontact(ph_book):
    c  = str(int(ph_book[len(ph_book)-1][0]) + 1)
    ph_book.append([0] * 0)

    match len(c):
        case 1:
            c = '00' + str(c)
        case 2:
            c = '0' + str(c)
        case '3':
            c = str(c)

    ph_book[len(ph_book)-1].insert(0, c)
    return ph_book

for i in range(5):
    c = view.input_value('write ')
    ph_book[len(ph_book)-1].insert(i+1, c)

print(ph_book)


# Сортировка списка строками
# names = ["Стив", "Рейчел", "Майкл", "Адам", "Джессика", "Лестер"]
# names.sort()
# print(names)
# ['Адам', 'Джессика', 'Лестер', 'Майкл', 'Рейчел', 'Стив']


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
 