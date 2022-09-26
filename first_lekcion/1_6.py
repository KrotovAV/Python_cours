a = 123456
b = 0

print(a)
print(b)
print('-----------')

while a != 0: # != не равен
    b = b * 10 + a % 10
    a //= 10
    print(a)
    print(b)
    print('********')
else:
    print('stop')
print(a)
print(b)
print('-----------')