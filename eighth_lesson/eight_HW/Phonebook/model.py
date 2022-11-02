import controller

# menu = "0. Показать все контакты: 1. Открыть файл с контактами: 2. Записать файл с контактами: 3. Добавить контакт: 4. Изменить контакт: 5. Удалить контакт: 6. Поиск по контактам'"

def main():
    path = 'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'
    with open(path,'r', encoding='utf8') as text:
        text = text.read()
    text = text.replace(' ','')
    # print(text)

    list_text = text.splitlines()
    for i in range(len(list_text)):
        list_text[i] = list_text[i].split('|')
    # print('main=',list_text)
    return list_text


def show_all(list_list):
    # if list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1] == '\n':
    #     print('xxxx')
    #     # list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1]
    #     list_list[len(list_list)-1].pop()

    # print(list_list)
    list_b = []
    for j in range(6):
        list_b.append(max([len(list_list[i][j]) for i in range(len(list_list))]))

    for i in range(len(list_list)):
        for j in range(6):
            if list_b[j] != len(list_list[i][j]):
                list_list[i][j] = list_list[i][j]+ ' '*(list_b[j] -len(list_list[i][j]))
        if list_list[i][-1] != '\n':
            list_list[i].append('\n')
    text_str = ''.join(list(map(lambda x: '|'.join(x), list_list)))
    # if list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1] == '\n':
    #     print('xxxx')
    #     # list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1]
    #     list_list[len(list_list)-1].pop()
    return text_str

def replace(list_list):
    for i in range(len(list_list)):
        for j in range(len(list_list[i])):
            list_list[i][j]= list_list[i][j].replace('|','')
    if list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1] == '\n':
        print('xxxx')
        # list_list[len(list_list)-1][len(list_list[len(list_list)-1])-1]
        list_list[len(list_list)-1].pop()

    return list_list

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