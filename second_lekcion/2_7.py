# Словари

dictionary = {} 
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    } 

print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} print(dictionary['left'])  # ←
# типы ключей могут отличаться

print(dictionary['up'])   # ↑ # типы ключей могут отличаться

dictionary['left'] = '⇐' 
print(dictionary['left'])  # ⇐ #print(dictionary['type'])  

# KeyError: 'type' del dictionary['left'] # удаление элемента

# (k,v) - ключ и значения

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item])) 

# up: ↑
# down: ↓
# right: →
# left: ←

for v in dictionary: # for (v) in dictionary.items():
    print(dictionary[v])

# ↑
# ↓
# →
# ←

print(dictionary['up'])
dictionary['up'] = '*'
print(dictionary['up'])