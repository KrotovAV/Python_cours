import controller
# ':Показать все контакты, '1': Открыть файл с контактами,
#                     '2': Записать файл с контактами, '3': Добавить контакт,
#                     '4': Изменить контакт, '5': Удалить контакт, '6': Поиск по контактам}
men0 = '         -------------- ------------- ------------ ------------- ------------ ----------- ------------- ----------'
menu = "         | 1. Показать | 2. Добавить | 3. Поиск   | 4. Изменить | 5. Удалить |6. Открыть | 7. Сохранить|    8.   |"
men2 = "         | все конт-ты |   контакт   | по конт-ам |   контакт   |  контакт   |    файл с контактами    |  выход  |"
def show_menu():
    # print()
    print(men0)
    print(menu)
    print(men2)
    print(men0)
    print()

nenu_se0 = '                                 -------- -------- ------------- ------------ ---------- ---------- ------------'
nenu_sea = '                                 | 1. №  | 2. Имя | 3. Отчество | 4. Фамилия | 5. №тел. | 6.Заметки| 7. по всем|'
def search_menu():
    print(nenu_se0)
    print(nenu_sea)
    print(nenu_se0)

menu_chang0 = '                                                  ---------- ------------'
menu_change = '                                                  | 1. По № | 2 Поиском |'
def change_menu():
    print(menu_chang0)
    print(menu_change)
    print(menu_chang0)

def input_value(string:str):
    while True:
        try:
            value = (input(string))
            return value
        except:
            print('Error, try again')

def change_value( change_string, nam_i, nam_j, string:str):
    # print(change_string[nam_i][nam_j])
    change_string[nam_i][nam_j] = (input(string))
    # inp = (input(string))
    # if c != '':
    #     change_string[nam_i][nam_j] = inp
    return change_string[nam_i][nam_j]

def print_values(var):
    print(var)

def print_empty():
    print('')