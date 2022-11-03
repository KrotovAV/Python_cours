
list_list = [['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки'], 
        ['001', 'Сергей', 'Сергеевич', 'Сергеев', '24585822', 'сосед'], 
        ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий'],
        ['003', 'Стас', 'Стасович', 'Стасов', '25698742', 'дача'],
        ['004',' ОльгаСер', 'Олегсоовна', 'Олегович', '74854925', 'парикмахер']]

# list_list = [['1.№', '2.Имя', '3.Отчество', '4.Фамилия', '5.№тел.', '6.Заметки\n'], ['001', 'Сергей', 'Сергеевич', 'Сергеев', '24585822', 'сосед\n'], ['002', 'Иванна', 'Ивановна', 'Иванова', '25896587', 'рабочий\n'], ['003', 'Стас', 'Стасович', 'Стасов', '25698742', 'дача\n'], ['004', ' ОльгаСер', 'Олегсоовна', 'Олегович', '74854925', 'парикмахер\n']]


print()

print(list_list)

print(list_list[0][-1][:-2])
print(list_list[0][-1][-2:])
list_list[0][-1] = list_list[0][-1][:-2] + ' '*5 + list_list[0][-1][-2:]
print(list_list[0][-1])
# print()
# for i in range(len(list_list[0])-1):
#     if list_list[i][-1][-1:] != '\n':
#         # print(list_list[i][-1][-1:])
#         list_list[i][-1] = list_list[i][-1] + '\n'
#         # print(list_list[i][-1])
#     # else:
#     #     # list_list[i][-1] = list_list[i][-1][:-2] + '\n'
#     #     list_list[i][-1] = list_list[i][-1]
#         # print(list_list[i][-1])
# # text_str = ''.join(list(map(lambda x: '|'.join(x), list_list)))
# print(list_list)
print()
# print(text_str)
# print(type(text_str))
# list_list = text_str

# print('x=',list_list[0][-1][-2:])
# print(list_list[0][-1][:-2])
print()

# for i in range(len(list_list[0])-1):
#     if list_list[i][-1][-1:] != '\n':
#         # print(list_list[i][-1][-1:])
#         list_list[i][-1] = list_list[i][-1] + '\n'
#         # print(list_list[i][-1])
#     # else:
#     #     # list_list[i][-1] = list_list[i][-1][:-2] + '\n'
#     #     list_list[i][-1] = list_list[i][-1]
#     #     # print(list_list[i][-1])

# print(list_list)
# print()
