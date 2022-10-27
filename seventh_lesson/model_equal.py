import view
import logger

x = 0
z = 0
equal = 0

dict_eq = {'*': 1, '/': 2, '+': 3, '-':4, "=": 5}

def check_namber(nam):
    if not nam.isdigit():
        view.err_namber()
        nam = view.get_namber()
    return nam

def check_action(act):
    if act not in ['+', '-', '*', '/', '=']:
        view.err_action()
        act = view.get_action()
    return act

def def_zero(acti, namb):
    eq = dict_eq.get(acti)
    if eq == 2 and int(namb) == 0:
        view.err_div_ze()
        logger.logger('error, division by zero')
        namb = view.get_namber()
    return namb

def init(a, c):
    global x
    global z
    x = a
    z = c

def do_it():
    equal = dict_eq.get(z)
    res = float(x)
    w = ''
    str_nam_eq = str(x) +' '+ z
    while equal != 5:
        yy = check_namber(view.get_namber())
        y = def_zero(w, yy)
        
        if equal == 1: res = res * float(y)
        if equal == 2: res = res / float(y)
        if equal == 3: res = res + float(y)
        if equal == 4: res = res - float(y)

        print('---        (', res,')')
        w = check_action(view.get_action())
        equal = dict_eq.get(w)
        str_nam_eq = str_nam_eq +' '+ y +' '+ w
        logger.logger(f'{str_nam_eq} { res}')
    return str_nam_eq, res
