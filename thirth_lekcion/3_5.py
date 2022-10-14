# Функция ﬁlter

# Функция ﬁlter() применяет указанную функцию к каждому 
# элементу итерируемого объекта и возвращает итератор с 
# теми объектами, для которых функция вернула True.

# f(x) ⇒ x - чётное 
# filter(f, [ 1, 2, 3, 4, 5])
#         [    2,    4  ]
# Нельзя пройтись дважды

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res= list(map(lambda x: (x , x ** 2), res))
print(res)


data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))
print(res)

