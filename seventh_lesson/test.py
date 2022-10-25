
dict_eq = {'*': 1, '/': 2, '+': 3, '-':4, "=": 5}

print('Write a namber'); 
a = int(input())
res = 0
print('Write equal');
c = input()
equal = dict_eq.get(c)

str_nam_eq= str(a) + c
while equal != 5:
    print('-------')
    print('Write a namber'); 
    b = int(input())

    if equal == 1: res = a * b
    if equal == 2: res = a / b
    if equal == 3: res = a + b
    if equal == 4: res = a - b
    print('==============')

    print('Write equal'); 
    c = input()
    equal = dict_eq.get(c)
    # print(equal)
    str_nam_eq = str_nam_eq + str(b) + c

print(str_nam_eq,res)