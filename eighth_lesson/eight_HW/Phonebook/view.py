import controller

men0 = '         ------------- ------------- ------------- ------------ ------------- ------------ ------------- ----------'
menu = "         | 1. Открыть | 2. Показать | 3. Добавить | 4. Поиск   | 5. Изменить | 6. Удалить | 7. Сохранить|    8.   |"
men2 = "         |    файл    | все конт-ты |   контакт   | по конт-ам |   контакт   |  контакт   |   в файл    |  выход  |"
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

menu_re0 = '                                                 ------------------ ----------------- ----------------------------'
menu_rec = '                                                 | 1. По умолчанию | 2. Выбрать файл | 3. Присвоить по умолчанию |'
def rec_menu():
    print(menu_re0)
    print(menu_rec)
    print(menu_re0)

menu_op0 = '         ------------------ ----------------- --------------------------'
menu_ope = '         | 1. По умолчанию | 2. Выбрать файл |3. Присвоить по умолчанию|'
def op_menu():
    print(menu_op0)
    print(menu_ope)
    print(menu_op0)

default_ope_path = '/eight_HW/Phonebook/phonebook.txt'
# default_ope_path = 'D:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'
# default_rec_path = '\eight_HW\Phonebook\phonebook.txt'
default_rec_path = 'D:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'

def input_value(string:str):
    while True:
        try:
            value = (input(string))
            return value
        except:
            print('Error, not from 1 to 8. Try again')

def change_value( change_string, nam_i, nam_j, string:str):
    change_string[nam_i][nam_j] = (input(string))
    return change_string[nam_i][nam_j]

def print_values(var):
    print(var)

def print_empty():
    print('')
