import controller

# menu = "0. Показать все контакты: 1. Открыть файл с контактами: 2. Записать файл с контактами: 3. Добавить контакт: 4. Изменить контакт: 5. Удалить контакт: 6. Поиск по контактам'"

def main():
    path = 'D:/GeekBrains\My Git/2 znakomstvo s iazikami/02 python/Python_cours/eighth_lesson/eight_HW/Phonebook/phonebook.txt'
    with open(path,'r', encoding='utf8') as text:
        text = text.read()
    text = text.replace(' ','')
    return text

def my_split(text):
    list_text = text.splitlines()
    for i in range(len(list_text)):
        list_text[i] = list_text[i].split('|')
    for i in range(len(list_text)):
        list_text[i][-1] = list_text[i][-1] + '\n'
    return list_text

def show_all(list_list):
    print(list_list)
    list_b = []
    for j in range(len(list_list[0])):
        print(max([len(list_list[i][j]) for i in range(len(list_list))]))
        list_b.append(max([len(list_list[i][j]) for i in range(len(list_list))]))
    for i in range(len(list_list)):
        for j in range(len(list_list[i])):
            if list_b[j] != len(list_list[i][j]):
                if j == len(list_list[i]) - 1:
                    list_list[i][-1] = list_list[i][-1][:-1] + ' '*(list_b[j] -len(list_list[i][j])) + list_list[i][-1][-1:]
                else:
                    list_list[i][j] = list_list[i][j]+ ' '*(list_b[j] -len(list_list[i][j]))
    text_str = ''.join(list(map(lambda x: '|'.join(x), list_list)))
    return text_str


def add_kontact(ph_book):
    c = str(int(ph_book[len(ph_book)-1][0]) + 1)
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

def search(ph_book_list, val, val_search):
    j = int(val) - 1
    res_list = [ph_book_list[0]]
    if val == '7':
        for i in range(1, len(ph_book_list)):
            for j in range(len(ph_book_list[i])):
                if val_search in ph_book_list[i][j]:
                    nam_i = i
                    res_list.append(ph_book_list[i])
                    break
    else:
        for i in range(1, len(ph_book_list)):
            if val_search in ph_book_list[i][j]:
                nam_i = i
                res_list.append(ph_book_list[i])
    if len(res_list) == 1:
        se = res_list.append([val_search,' NOT ',' FOUND ','','',''])
        nam_i = 0
    se = (''.join(list(map(lambda x: '|'.join(x), res_list))))
    return se, nam_i

def renumerate(ph_book):
    for i in range(2,len(ph_book)):
        c = str(int(ph_book[i][0]))
#     print(c)
#     print('l=', len(c))
        match len(c):
            case 1:
                c = '00' + str(c)
            case 2:
                c = '0' + str(c)
            case '3':
                c = str(c)
        ph_book[i][0] = c
    return ph_book