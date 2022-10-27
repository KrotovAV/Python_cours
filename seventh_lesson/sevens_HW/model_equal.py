import view
import logger
import operator
import re

x = 0
z = 0
equal = 0

dict_eq = {'*':operator.mul, '/':operator.truediv, '+':operator.add, '-':operator.sub, '=':5}

def check_namber(nam):
    nam_nam = nam.replace(".", "", 1)
    while (len(re.findall(r'[a-zA-Z!@#$%^&?х}\{/.,/]', nam_nam.replace(" ", "")))) != 0:
        nam_nam = nam.replace(".", "", 1)
        # print(nam_nam)
        # print(type(nam_nam))
        if not nam_nam.lstrip('+-').isdigit(): 
            view.err_namber()
            nam = view.get_namber()
    return nam


def exam(nam):
    if len(re.findall(r'[0-9\.]+|[^0-9\.]+', nam))>2:
        res = calculation(nam)
        view.exam_pri(nam, res)
        logger.logger(f'({nam}) = {res}')
    else:
        res = nam
    return res

def check_action(act):
    while act not in ['+', '-', '*', '/', '='] != True:
        if act not in ['+', '-', '*', '/', '=']:
            view.err_action()
            act = view.get_action()
    return act

def def_zero(acti, namb):

    while dict_eq.get(acti) == operator.truediv and int(namb) == 0:
        if dict_eq.get(acti) == operator.truediv and int(namb) == 0:
            view.err_div_ze()
            logger.logger('error, division by zero')
            namb = view.get_namber()
    return namb

def arithm(strin, eq_str):
        l = len(strin)-2
        n = 0
        while n < l:
            if strin[n+1] == eq_str:
                strin[n] =  dict_eq[eq_str](float(strin[n]), float(strin[n+2]))
                strin.pop(n+1)
                strin.pop(n+1)
                n = 0
                l =  l - 2
            else:
                n = n + 1
        # print(strin)
        return strin


def calculation(stri):
    list2 = re.findall(r'[0-9\.]+|[^0-9\.]+', stri.replace(" ", ""))
    list2.append(' ')
    list2.append(' ')
    # print(list2)
    if list2[0] == '+' or list2[0] == '-': list2.insert(0,'0')
    list2 = arithm(list2, '*')
    list2 = arithm(list2, '/')
    list2 = arithm(list2, '-')
    list2 = arithm(list2, '+')
    res = float(list2[0])
    # print(res)
    # print()
    return res

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
        yyy = exam(yy)
        y = str(def_zero(w, yyy))
        
        res =  equal(res, float(y))

        print('---        (', res,')')
        w = check_action(view.get_action())
        equal = dict_eq.get(w)
        str_nam_eq = str_nam_eq +' '+ y +' '+ w
        logger.logger(f'{str_nam_eq} { res}')
    return str_nam_eq, res
