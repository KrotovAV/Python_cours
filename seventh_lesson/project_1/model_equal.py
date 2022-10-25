import view
import logger

x = 0
z = 0
equal = 0

dict_eq = {'*': 1, '/': 2, '+': 3, '-':4, "=": 5}

def init(a, c):
    global x
    global z
    x = a
    z = c

def do_it():
    # res = 0
    equal = dict_eq.get(z)
    res = int(x)
    str_nam_eq= str(x) +' '+ z

    while equal != 5:
        y = view.get_value()
        if not y.isdigit():
            view.err_value()
            y = view.get_value()
        if equal == 2 and int(y) == 0:
            view.err_div_ze()
            logger.logger('error, division by zero')
            y = view.get_value()
        if equal == 1: res = res * int(y)
        if equal == 2: res = res / int(y)
        if equal == 3: res = res + int(y)
        if equal == 4: res = res - int(y)
        print('---        (', res,')')
 
        w = view.get_action()
        if w not in ['+', '-', '*', '/', '=']:
            view.err_action()
            w = view.get_action()
        equal = dict_eq.get(w)
        str_nam_eq = str_nam_eq +' '+ str(y) +' '+ w
        logger.logger(f'{str_nam_eq}, { res}')
    return str_nam_eq, res
