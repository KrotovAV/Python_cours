import random
l = list(range(1, 10))
random.shuffle(l)
for i in l:
    print(i, end=', ')