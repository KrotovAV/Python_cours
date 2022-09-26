# Логические операции
# >, >=, <, <=, ==, != 
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

a = 1 < 3 and 5 >2
print(a)

b = 1 == 2
print(b)

c = 1 != 2
print(c)

d = 'abc'
e = 'abc'
print(d == e)

f = 1 < 3 < 5 < 10
print(f)

g = 1 < 3 or 5 > 10
print(g)

h = [1, 3, 7, 16]
print(2 in h)
print(3 in h)
print(not 6 in h)

is_odd = h[3] % 2 == 0
print(is_odd)