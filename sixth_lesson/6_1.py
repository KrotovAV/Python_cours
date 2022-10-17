# 1. Ввести с клавиатуры 2 числа (int) и вывести в клнсоль их НОК (найменьшее общее кратное)


print()
# print('Write first  namber')
n = int(input('Write first  namber '))

# print('Write second  namber')
m = int(input('Write second  namber '))
print('---------------------------')

i = 1

while(min(n, m)*i%max(m, n)):
    i +=1

print(f'нок для {m} и {n} будет {min(n,m)*i}' )
print() 