print()
from queue import Empty
import random
n = random.randint(1, 10)
print('n = ', n)

# i = 0
list = []
for i in range(n):
    list.append(random.randint(1, 999))
print(list)

strin = str()
for i in range(n):
    strin =strin + ' ' + str(list[i])

strin = strin.replace(' ', '', 1) 

print(strin)
print(type(strin))
print('----------')

with open('4_11.txt', 'w') as file:
    file.write(strin)
