import model
import view

print()
# ph_book = [['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки'], 
#         ['001', 'Сергей', 'Сергеевич', 'Сергеев', '24585822', 'сосед'], 
#         ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий'],
#         ['004', 'Стас', 'Стасович', 'Стасов', '25698742', 'дача'],
#         ['005','Ольга Сергей', 'Олеговна', 'Олегович', '74854925', 'парикмахер']]
# [[' 1.№ ', ' 2.Имя  ', ' 3.Отчество ', ' 4.Фамилия ', ' 5.№тел.  ', ' 6.Заметки ', '\n'], [' 001 ', ' Серей  ', ' Сергеевич  ', ' Сергеев   ', ' 24585822 ', ' сосед     ', '\n'], [' 002 ', ' Иванна ', ' Ивановна   ', ' Иванова   ', ' 25896587 ', ' рабочий   ', '\n'],
# ['003', 'f', 'bfbfb', 'bdsba', 'vadsvad', 'dv', '\n']]

# op_rec_dict = {1:'D:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt',2:'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook2.txt', 3:'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook3.txt'}
# print(op_rec_dict)

# var = view.input_value('choose an action ')

def verify_choose(cho):
    while cho == int(cho):
        if 0 > int(cho) > 8:
            print('Try again')
        # else:
            # return cho
    return cho

def input_value(string:str):
    while True:
        try:
            value = int(input(string))
            return value
        except:
            print('Error, try again')

# var = verify_choose(var)
# print(var)

v =input_value('choose an action ')
print(v)