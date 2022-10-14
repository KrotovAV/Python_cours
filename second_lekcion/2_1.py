# Связать файловую переменную с файлом, определив модификатор работы 
# a – открытие для добавления данных 
# r – открытие для чтения данных 
# w – открытие для перезаписи данных 
# --------------------

# with open('file.txt', 'a') as data:
#     data.write('line 1fg8\n')
#     data.write('line 2fgy8\n')
# #-----------------------------
# colors = ['red', 'green', 'blue'] 
# data = open('file.txt', 'a') 
# data.writelines(colors) # разделителей не будет data.close()
# data.close()
# ---------------------
# lines = ["first", "second", "third"] # Запись построчно
# with open(r"D:\test.txt", "w") as file:
#     for  line in lines:
#         file.write(line + '\n')


# ---------------------
# colors = ['red', 'green', 'blue123'] 
# data = open('file.txt', 'a') 
# # data.writelines(colors) # разделителей не будет data.close()
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()


# ---------------------
# colors = ['red', 'green', 'blue'] 
# data = open('file.txt', 'w') 
# data.writelines(colors) # разделителей не будет 
# data.close()
# -------------

# path = 'file.txt' 
# data = open(path, 'r') 
# for line in data: 
#     print(line) 
# data.close()