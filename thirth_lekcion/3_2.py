# В файле хранятся числа, нужно выбрать четные и 
# составить список пар (число; квадрат числа). Пример:
# 1 2 3 5 8 15 23 38 
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

path = 'D:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/f.txt'
f = open(path, 'r') 
data = f.read() + ' ' 
f.close()
# print(data)
# print(type(data))
numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
print(data)
out = [] 
for e in numbers:
    if not e % 2:
        out.append((e,e **2)) 
print(out)





# data = select(int, data) 
# data = where(lambda e: not e % 2, data) 
# data = list(select(lambda e: (e, e**2), data))

# def select(f, col):
# return [f(x) for x in col]
# def where(f, col):
#   return [x for x in col if f(x)]
#   data = '1 2 3 5 8 15 23 38'.split() 
#   data = select(int, data) 
# data = where(lambda e: not e % 2, data) 
# data = list(select(lambda e: (e, e**2), data))

# data = '1 2 3 5 8 15 23 38'.split() 
# data = list(map(int, data)) 
# data = list(filter(lambda e: not e % 2, data)) data = list(map(lambda e: (e, e**2), data)) print(data)
