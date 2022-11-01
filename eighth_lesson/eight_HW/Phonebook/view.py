import controller
# ':Показать все контакты, '1': Открыть файл с контактами,
#                     '2': Записать файл с контактами, '3': Добавить контакт,
#                     '4': Изменить контакт, '5': Удалить контакт, '6': Поиск по контактам}
men0 = '         -------------- ------------- ------------- ------------ ------------ ---------------- -----------'
menu = "         | 1. Показать | 2. Добавить | 3. Изменить | 4. Удалить | 5. Поиск   | 6. Сохранить   |    7.   |"
men2 = "         | все конт-ты |   контакт   |   контакт   |   контакт  | по конт-ам | файл с конт-ми |  выход  |"
def show_menu():
    print()
    print(men0)
    print(menu)
    print(men2)
    print(men0)
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