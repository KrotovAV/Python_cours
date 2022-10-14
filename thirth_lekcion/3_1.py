# Анонимные, lambda функции

def calk1(x):
    return x+10

print(calk1(10))

def calk2(x):
    return x*10

print(calk2(10))

print('------------')
def math(op, x):
    print(op(x))

math(calk2, 10)
math(calk1, 10)
print('------------')

def sum(x, y):
    return(x + y)

f = sum
sum2 = lambda x, y: x + y

def mylt(x, y):
    return(x * y)

def calc(op, a, b,):
    print(op(a, b))
    # return op(a,b)

calc(mylt, 4, 5)
calc(f, 4, 5)
calc(sum2, 4, 5)
calc(lambda x, y: x + y, 4, 5)
print('------------')

sum = lambda x: x+10
mult = lambda x: x**2
sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

sum4 = lambda x: x+242
mult4 = lambda x: x**5
sum3(mult2(2))

