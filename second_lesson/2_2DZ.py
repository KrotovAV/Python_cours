# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 

trigger = True

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) != (not x) and (not y) and (not z):
                print('Не верно')
                trigger = False

if trigger: print('всегда верно')