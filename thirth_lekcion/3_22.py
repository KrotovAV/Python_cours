# В файле хранятся числа, нужно выбрать четные и 
# составить список пар (число; квадрат числа). Пример:
# 1 2 3 5 8 15 23 38 
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res= select(lambda x: (x , x ** 2), res)
# print(res)

li = [x for x in range(1, 20)]

li = list(map(lambda x:x+10, li))
print(li)

# data = input().split() # о умолчанию символ разделитель пробел
# data = input().split(',') # символ разделитель pfgznfz
data = list(map(int, input().split()))
print(data)