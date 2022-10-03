# функции с любым количеством аргументов

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))  

# asdw print(concatenatio('a', '1', 'd', '2'))  
# # a1d2 # print(conatenatio(1, 2, 3, 4)) 
# # TypeError: ..