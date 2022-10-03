# аргументы по умолчанию

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!! 
# print(new_string('!'))      # TypeError missing 1 required ...

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!! 
print(new_string('!'))      # TypeError missing 1 required ...