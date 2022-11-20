# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy  as np
from math import sqrt

# f(x) = a*x**4*sin(cos(x)) + b*x**3 + c*x**2 + d*x + e

a = -12
b = 18
c = 5
d = 10
e = -30
x_start = -10
x_step = 0.1
x_end = 10 + x_step

print('-----------------------------')
print(f'f(x) = {a}*x^4*sin(cos(x)) + {b}*x^3 + {c}*x^2 + {d}^x + {e}')

def funkcion(x_f, a_f, b_f, c_f, d_f, e_f):
    y_f = a_f*x_f**4*np.sin(np.cos(x_f)) + b_f*x_f**3 + c_f*x_f**2 + d_f*x_f + e_f
    return y_f

print('-----------------------------')

# 1. корни уровнения

def solve(a_f, b_f, c_f, d_f, e_f, x_start_f, x_end_f, x_step_f):
    for x_f in np.arange(x_start_f, x_end_f, x_step_f):
        # if 0 == a_f*x_f**4*np.sin(np.cos(x_f)) + b_f*x_f**3 + c_f*x_f**2 + d_f*x_f + e_f
        if 0 == funkcion(x_f, a_f, b_f, c_f, d_f, e_f):
            return x_f
        else:
            return None

root = solve(a, b, c, d, e, x_start, x_end, x_step)
print('root=', root)
print('-----------------------------')

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает

def funkcion_growing_decreases(a_f, b_f, c_f, d_f, e_f, x_start_f, x_end_f, x_step_f):
    # x_list = [x for x in np.arange(x_start_f, x_end_f, x_step_f)] + [x_end_f + x_step_f]
    x_list = [x_start_f - x_step_f] + [x for x in np.arange(x_start_f, x_end_f, x_step_f)] + [x_end_f + x_step_f]
    # print(x_list)
    
    x_list_gro_f = []
    x_list_dec_f = []

    def f_n(x):
        return funkcion(x_list[x], a_f, b_f, c_f, d_f, e_f)
    def f_m(x):
        return funkcion(x_list[x-1], a_f, b_f, c_f, d_f, e_f)
    def f_p(x):
        return funkcion(x_list[x+1], a_f, b_f, c_f, d_f, e_f)
 
    time_s_g = x_list[0]
    time_s_d = x_list[0]

    for i in range(1, len(x_list)-1):
        if f_m(i) > f_n(i) and f_n(i) < f_p(i):
            time_s_g = x_list[i]
        if f_m(i) < f_n(i) and f_n(i) > f_p(i):
            t_time_g = time_s_g, x_list[i]
            x_list_gro_f.append(t_time_g)
        if i == len(x_list)-2 and f_m(i) < f_n(i):
            t_time_g = time_s_g, x_list[i+1]
            x_list_gro_f.append(t_time_g)

        if f_m(i) < f_n(i) and f_n(i) > f_p(i):
            time_s_d = x_list[i]
        if f_m(i) > f_n(i) and f_n(i) < f_p(i):
            t_time_d = time_s_d, x_list[i]
            x_list_dec_f.append(t_time_d)
        if i == len(x_list)-2 and f_m(i) > f_n(i):
            t_time_d = time_s_d, x_list[i+1]
            x_list_dec_f.append(t_time_d)

    return x_list_gro_f, x_list_dec_f

x_list_gro, x_list_dec = funkcion_growing_decreases(a, b, c, d, e, x_start, x_end, x_step)
print('growing intervals =', x_list_gro)
print('decreases intervals =',x_list_dec)
print('-----------------------------')

# 5. Вычислить вершину

def max_min(a_f, b_f, c_f, d_f, e_f, x_start_f, x_end_f, x_step_f):
    x_list = [x for x in np.arange(x_start_f, x_end_f, x_step_f)]

    max_x = x_list[0]
    for i in range(len(x_list)-1):
        if funkcion(x_list[i], a_f, b_f, c_f, d_f, e_f) > funkcion(max_x, a_f, b_f, c_f, d_f, e_f):
            max_x = x_list[i]

    min_x = x_list[0]
    for i in range(len(x_list)-1):
        if funkcion(x_list[i], a_f, b_f, c_f, d_f, e_f) < funkcion(min_x, a_f, b_f, c_f, d_f, e_f):
            min_x = x_list[i]

    return max_x, min_x

max_x, min_x = max_min(a, b, c, d, e, x_start, x_end, x_step)
print('max_x = ',max_x)
print('min_x = ',min_x)
print('-----------------------------')

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

def funkcion_positive_negative(a_f, b_f, c_f, d_f, e_f, x_start_f, x_end_f, x_step_f):
    x_list = [x_start_f - x_step_f] + [x for x in np.arange(x_start_f, x_end_f, x_step_f)] + [x_end_f + x_step_f]
#     # print(x_list)
    
    x_list_pos_f = []
    x_list_neg_f = []

    def f_n(x):
        return funkcion(x_list[x], a_f, b_f, c_f, d_f, e_f)
    def f_m(x):
        return funkcion(x_list[x-1], a_f, b_f, c_f, d_f, e_f)
    def f_p(x):
        return funkcion(x_list[x+1], a_f, b_f, c_f, d_f, e_f)
 
    time_s_p = x_list[0]
    time_s_n = x_list[0]

    for i in range(1, len(x_list)-1):
        if f_m(i) <= 0 and f_n(i) > 0:
            time_s_p = x_list[i]
        if f_n(i) > 0 and f_p(i) <= 0:
            t_time_p = time_s_p, x_list[i+1]
            x_list_pos_f.append(t_time_p)

        if f_m(i) >= 0 and f_n(i) < 0:
            time_s_n = x_list[i]
        if f_n(i) < 0 and f_p(i) >= 0:
            t_time_n = time_s_n, x_list[i+1]
            x_list_neg_f.append(t_time_n)

    return x_list_pos_f, x_list_neg_f

x_list_pos, x_list_neg = funkcion_positive_negative(a, b, c, d, e, x_start, x_end, x_step)
print('positive intervals =', x_list_pos)
print('negative intervals =',x_list_neg)
print('-----------------------------')

# 4. постоить график

# график всё
x = np.arange(x_start, x_end, x_step)
y = funkcion(x, a, b, c, d, e)

plt.plot(x, y, 'g', label = 't')
plt.grid()
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
# plt.show()

#гдафик положительые - отрицательные
for i in range(len(x_list_pos)):
    cur_x = np.arange(x_list_pos[i][0], x_list_pos[i][1] + x_step, x_step)
    y = funkcion(cur_x, a, b, c, d, e)
    plt.plot(cur_x, funkcion(cur_x, a, b, c, d, e), 'b', label = 't')

for i in range(len(x_list_neg)):
    cur_xx = np.arange(x_list_neg[i][0], x_list_neg[i][1]+ x_step, x_step)
    yy = funkcion(cur_xx, a, b, c, d, e)
    plt.plot(cur_xx, yy, 'r', label = 't')
plt.grid()
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
# plt.show()

#гдафик возрастание - убывание
for i in range(len(x_list_gro)):
    cur_x = np.arange(x_list_gro[i][0], x_list_gro[i][1] + x_step, x_step)
    y = funkcion(cur_x, a, b, c, d, e)
    plt.plot(cur_x, funkcion(cur_x, a, b, c, d, e), 'b', label = 't')

for i in range(len(x_list_dec)):
    cur_xx = np.arange(x_list_dec[i][0], x_list_dec[i][1]+ x_step, x_step)
    yy = funkcion(cur_xx, a, b, c, d, e)
    plt.plot(cur_xx, yy, 'r', label = 't')
plt.grid()
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()

