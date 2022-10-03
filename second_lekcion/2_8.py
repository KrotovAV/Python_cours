# Множества - Неупорядоченная совокупность элементов
              #  изменяемые

a = {1, 2, 3, 5, 8} 
b = {'2', '5', 8, 13, 21} 
print(type(a))  # set 
print(type(b))  # set

colors = {'red', 'green', 'blue'} 
print(colors)   # {'red', 'green', 'blue'} 

colors.add('red') 
print(colors)   # {'red', 'green', 'blue'} 

colors.add('gray') # добавить элемент
print(colors)   # {'red', 'green', 'blue','gray'} 

colors.remove('red') # убрать элемент
print(colors)   # {'green', 'blue','gray'}

# colors.remove('red') # KeyError: 'red' 

colors.discard('red')  # ok 
print(colors)   # {'green', 'blue','gray'} 

colors.clear()   # { } # очистить множество
print(colors)   # set()