# напишите программу, которая удаляет из текста все слова содержащие "абв"

# text = 'Сюжет славянских кумулятивных сказок, построенный \
# + на нагнетании повторяющихся эпизодов. Сказки известны и в фольклоре балтских, \
# + скандинавских, германских народов, а также в узбекском и татарском.'

# with open(filename, 'r', encoding='utf8') as f:
#     text = f.read()
   
print()

path = '5_2.txt'
with open(path,'r', encoding='utf8') as text:
    text = text.read() 
print(text)
   
print()
# print(text)
list_str = text.split(' ')
print(list_str)

f_text = 'а'

for i in list_str:
    if f_text in i:
        print()
        print(i)
        print()
        list_str.remove(i)
        # 
print(list_str)


   
print()