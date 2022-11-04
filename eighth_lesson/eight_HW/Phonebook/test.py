import model
import view


print()
ph_book = [['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки'], 
        ['001', 'Сергей', 'Сергеевич', 'Сергеев', '24585822', 'сосед'], 
        ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий'],
        ['004', 'Стас', 'Стасович', 'Стасов', '25698742', 'дача'],
        ['005','Ольга Сергей', 'Олеговна', 'Олегович', '74854925', 'парикмахер']]
# [[' 1.№ ', ' 2.Имя  ', ' 3.Отчество ', ' 4.Фамилия ', ' 5.№тел.  ', ' 6.Заметки ', '\n'], [' 001 ', ' Серей  ', ' Сергеевич  ', ' Сергеев   ', ' 24585822 ', ' сосед     ', '\n'], [' 002 ', ' Иванна ', ' Ивановна   ', ' Иванова   ', ' 25896587 ', ' рабочий   ', '\n'],
# ['003', 'f', 'bfbfb', 'bdsba', 'vadsvad', 'dv', '\n']]
val_i_del = 2
del_string = model.my_split(ph_book[val_i_del-1])
view.print_values(model.show_all(del_string))
print(ph_book)
# ph_book[0][0] = '001'
# print(ph_book[0][0])
# print(int(ph_book[0][0]))

# view.print_values(model.show_all((model.my_split(ph_book[val_i_del-1]))))

print()
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
 