import controller
# ':Показать все контакты, '1': Открыть файл с контактами,
#                     '2': Записать файл с контактами, '3': Добавить контакт,
#                     '4': Изменить контакт, '5': Удалить контакт, '6': Поиск по контактам}
menu0 = '         -------------- ------------- ------------- ------------- ------------- ------------ ----------- -----------'
menu = "         | 0. Показать | 1. Открыть  | 2. Записать | 3. Добавить | 4. Изменить | 5. Удалить | 6. Поиск  | 7. выход |"
men2 = "         | все конт-ты | файл с конт | файл с конт |   контакт   |   контакт   |  контакт   | по конт-ам| 7. выход |"
def show_menu():
    print()
    print(menu0)
    print(menu)
    print(men2)
    print(menu0)
    print()

def input_value(string:str):
    while True:
        try:
            value = (input(string))
            return value
        except:
            print('Error, try again')

def print_values(var):
    print(var)

def print_empty():
    print('')