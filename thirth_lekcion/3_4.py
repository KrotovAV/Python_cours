# List Comprehension

# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable if (conditional)]
# [exp <if conditional> for item in iterable if (conditional)]

list = []

for i in range(0, 21):
    if(i%2 == 0):
        list.append(i)

print(list)

list = [i for i in range(0, 21) if(i%2 == 0)]
print(list)
print('-----------------------')
list = [(i, i) for i in range(0, 21) if(i%2 == 0)]
print(list)

print('=======================')

def f(x):
    return x**3

list = [f(i) for i in range(1, 21) if(i%2 == 0)]
print(list)

list = [(i, f(i)) for i in range(1, 21) if(i%2 == 0)]
print(list)
print('=======================')