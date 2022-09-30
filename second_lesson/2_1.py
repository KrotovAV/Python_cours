a=[1, 2, 3]
b = a
a.append(4)
print(b)

list = [] # список
list.append(5)

dict = {} # словарь
dict[1] = 'Вова'
dict[23] = 'Петя'
dict[15] = 'Вася'
dict[1] = 'Маша'

print(list)
print(dict)
print(dict.get(15))
print(dict.get(10))

c = a.copy() # копирует
#c = a[:] # тоже копирует


a.append(5)
c.append(7)

print(a)
print(b)
print(c)

