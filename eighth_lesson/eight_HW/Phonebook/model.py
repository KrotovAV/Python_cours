import controller

# lau = {'Петер Хандке': '2019', 'Светлана Алексеевич': '2015',
#             'Шеймус Хини': '1995', 'Кэнзабуро Оэ': '1994', 'Тони Моррисон':
#             '1993', 'Дерек Уолкотт': '1992', 'Надин Гордимер': '1991'}

# dict_menu = {'0':Показать все контакты, '1': Открыть файл с контактами,
#                     '2': Записать файл с контактами, '3': Добавить контакт,
#                     '4': Изменить контакт, '5': Удалить контакт, '6': Поиск по контактам}

# menu = "0. Показать все контакты: 1. Открыть файл с контактами: 2. Записать файл с контактами: 3. Добавить контакт: 4. Изменить контакт: 5. Удалить контакт: 6. Поиск по контактам'"



def show_all():
    path = 'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'
    with open(path,'r', encoding='utf8') as text:
        text = text.read()
    # print(text)

    list_text = text.splitlines()
    for i in range(len(list_text)):
        list_text[i] = list_text[i].split('|')

    list_b = []
    for j in range( len(list_text)):
        a = max([len(list_text[i][j]) for i in range(len(list_text))])
        list_b.append(a)
    # print(list_b)

    for i in range(len(list_text)):
        for j in range(len(list_text)):
            list_text[i][j] = ' ' + list_text[i][j]+ ' '*(list_b[j]+1 -len(list_text[i][j]))
        list_text[i].append('\n')
    # print('----------------')

    text_str = ''.join(list(map(lambda x: '|'.join(x), list_text)))
    return text_str
