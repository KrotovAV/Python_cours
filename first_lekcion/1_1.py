print('')
print('hello')
print('')

#Типы данных справедливы int, float, boolean, str 
#list и др.
perem = None
a = 123
b = 1.23

print(a)
print(b)

perem = a + b

print(perem)
print('')
print(type(a))
print(type(b))
print(type(perem))
print('')

s = 'hello world'
print(s)
t = 'hello "world'
print(t)
r = "hello 'world"
print(r)
i = "hello \nworld"
print(i)
print('')
print(a, b, perem)

print('')
print(a,'-', b,'-', s)

print('')
print('{} - {} - {}'.format(a, b, s))

print('')
print('{1} - {2} - {0}'.format(a, b, s))

print('')
print(f'{a} - {b} - {s}')

print('')