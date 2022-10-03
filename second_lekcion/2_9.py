# операции над множествами

a = {1, 2, 3, 5, 8} 
b = {2, 5, 8, 13, 21} 
c = a.copy() # копирование c = {1, 2, 3, 5, 8}


u = a.union(b)          # объедирение u = {1, 2, 3, 5, 8, 13, 21} 
i = a.intersection(b)   # пересечение i = {8, 2, 5} dl = a.difference(b)# dl = {1, 3} 
dr = b.difference(a)    # различия dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b)) # {1, 21, 3, 13}

# множества неизменяемые

c = {1, 2, 3, 5, 8} 
d = frozenset(c) 
print(d) # frozenset({1, 2, 3, 5, 8})