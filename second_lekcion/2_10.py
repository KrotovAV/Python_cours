# Списки

list1 = [1,2,3,4,5,6]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

list1[0] = 123
print('-------')
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

print('-----------')

list2[1] = 345
print('-------')
for e in list1:
    print(e)
print()
for e in list2:
    print(e)
print('+++')
print(list1.pop(2))
print(list1)

print('=====')
print(len(list1))
print(list1.pop())
print(list1)
print('==1===')
print(list1.pop())
print(list1)
print('==2===')
print(list1.pop())
print(list1)
print('==3===')
print(list1.pop())
print(list1)

print(list1.insert(2, 11)) # добавляем элнемент в позицию 2
print(list1)

print(list1.append(13)) # добавляем элнемент в конец
print(list1)