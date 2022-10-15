# 2. Создайте программу для игры в 'Крестики-нолики'.

import random
print()

pl_fi = {'aa': 1 , 'ab': 2 , 'ac' : 3, 'ba' : 4 , 'bb' : 5 , 'bc' : 6 , 'ca' : 7, 'cb' : 8, 'cc' : 9, 'ad':'|', 'b': '------------------'}

print('')
print('')
print('-------------------START THE GAME---------------------')

print('')
print('')
print('             Press enter to continue')
e = input()
print('(To make a move, enter the field number (1 - 9) and press enter)')
print()
print()

print('                ',pl_fi.get('aa'),' ', pl_fi.get('ad'),' ', pl_fi.get('ab'),' ', pl_fi.get('ad'),' ', pl_fi.get('ac'))
print('                ',pl_fi.get('b'))
print('                ',pl_fi.get('ba'),' ', pl_fi.get('ad'),' ', pl_fi.get('bb'),' ', pl_fi.get('ad'),' ', pl_fi.get('bc'))
print('                ',pl_fi.get('b'))
print('                ',pl_fi.get('ca'),' ', pl_fi.get('ad'),' ', pl_fi.get('cb'),' ', pl_fi.get('ad'),' ', pl_fi.get('cc'))

a = random.randint(1, 2)

cou_list = []
cou = 0
w = 0
while w != 3 and cou <= 9:
    
    print()
    print()
    t = True

    if a == 1:
        print('          ','--------move cross (X)---------')
    else:
        print('          ','--------move zero (O)----------')
    print('')
    while t == True:
        print('    ', 'Enter the number and press enter to continue')
        c = (input())
        #------------------------
        if c.isdigit() != True:
            print("     !!! Error TEXT, enter the correct number from 1 to 9 !!!")
            print()
            t = True
            continue 
        #----------------------------
        c_int = int(c)
        if c_int > 9 or c_int < 0:
            print("     !!! Error, enter the correct number from 1 to 9 !!!")
            print()
            t = True
        else:
            t = False
        for i in range(len(cou_list)):
            if c_int == cou_list[i]:
                print("     !!!      Error, this number is already taken     !!!")
                print()
                t = True
        
    c = int(c)
    cou_list.insert(cou, c)
    
    key = str(list(pl_fi.keys())[list(pl_fi.values()).index(c)])
    
    if a == 1:
        pl_fi[key] = 'x'
    else:
        pl_fi[key] = 'O'

    print()
    print('                ',pl_fi.get('aa'),' ', pl_fi.get('ad'),' ', pl_fi.get('ab'),' ', pl_fi.get('ad'),' ', pl_fi.get('ac'))
    print('                ',pl_fi.get('b'))
    print('                ',pl_fi.get('ba'),' ', pl_fi.get('ad'),' ', pl_fi.get('bb'),' ', pl_fi.get('ad'),' ', pl_fi.get('bc'))
    print('                ',pl_fi.get('b'))
    print('                ',pl_fi.get('ca'),' ', pl_fi.get('ad'),' ', pl_fi.get('cb'),' ', pl_fi.get('ad'),' ', pl_fi.get('cc'))

    if a == 1:
        a = 2
    else:
        a = 1
 
    win = [pl_fi['aa'] , pl_fi['ab'], pl_fi['ac']] , [pl_fi['ba'] , pl_fi['bb'] , pl_fi['bc']] , [pl_fi['ca'] , pl_fi['cb'] , pl_fi['cc']], [pl_fi['aa'] , pl_fi['ba'] , pl_fi['ca']] , [pl_fi['ab'] , pl_fi['bb'] , pl_fi['cb']] , [pl_fi['ac'] , pl_fi['bc'] , pl_fi['cc']] , [pl_fi['aa'] , pl_fi['bb'] , pl_fi['cc']], [pl_fi['ca'] , pl_fi['bb'], pl_fi['ac']]
    # print(win)
    for i in range(len(win)):
        if win[i][0] == win[i][1]:
            if win[i][1] == win[i][2]:
                w = 3
    # print('w=', w)
    cou = cou + 1


print()
print()

if cou == 9:
    c = '!!!     ---     no winner     ---     !!!'
else:
    if a != 1:
        c = '!!! Congratulations, cross (X) winner !!!'
    else:
        c = '!!! Congratulations, zero (O) winner !!!'

print('   ','===============================================')
print('   ','=                                             =')
print('   ','= ', c, ' =')
print('   ','=                                             =')
print('   ','===============================================')

print()
print()
