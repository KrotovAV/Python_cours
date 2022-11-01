

def input_value(string:str):
    while True:
        try:
            value = int(input(string))
            return value
        except:
            print('Error, try again')

def print_values(variable: int):
    print(variable)
