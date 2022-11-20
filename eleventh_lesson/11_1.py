#!/usr/bin/env python
# coding: utf-8

# In[12]:


[x for x in range(i)]


# In[5]:


a = 7
b = 3


# In[10]:


i = 9


# # good

# In[28]:


import matplotlib.pyplot as plt
import numpy  as np


# In[29]:


x = np.arange(0, 10)
print(x)
y = np.arange(-10, 0)
print(y)


# In[32]:


plt.plot(x, y, 'r', label = 'TOP')
plt.show()


# In[ ]:


# from math import sqrt

# def func(x):
#     function = a*x**2 + b*x + c
#     return function
# x = 5
# def sqr_roots(a, b, c):
#     dscrt =  b*x**2 + a*x + c
#     if dscrt > 0:
#         x1 = (-b + math.sqrt(dscrt)) / (2 * a)
#         x2 = (-b - math.sqrt(dscrt)) / (2 * a)
#         return (x1, x2)
#     elif dscrt == 0:
#         x = -b / (2 * a)
#         return x
#     else:
#         return None

# sqr_roots(5, 10, -30)
# min_func = min(func(x))


# In[ ]:


f(x) = 5x^2 + 10x - 30
1 корни уровнения
2 постоить график
3 найти вершину
4 промежутки возрастания и убывания


# In[50]:


# f(x) = 5*x**2 + 10*x - 30


# In[142]:


# 1. корни уровнения
from math import sqrt
a = 5
b = 10
c = -30
def solve(a,b,c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    else:
        return 'вещественных коней нет'


# In[143]:


solve(a, b, c)
print(solve(a, b, c))

x = np.arange(-4, 5, 0.1)
# print(x)


# In[131]:


# 2. постоить график
plt.plot(x, y, 'r', label = 't')

plt.show


# In[112]:


# 3. найти вершину

#(5, 10, -30)

def x_max(a, b):
    return -b/(2*a)

max_x = x_max(5, 10)
print('max_x = ',max_x)

def func(x, a, b, c):
    return a* x **2 + b*x + c

# x = x_max(5, 10)
# print(func(x , 5, 10, -30))
max_y = func(x_max(5,10), 5, 10, -30)
print('max_y =', max_y)


# In[128]:


negative_x = np.arange(-10, max_x, 0.1)
positive_x = np.arange(max_x, 10, 0.1)

# print(negative_x)
# print(positive_x)


# In[134]:


def func(x, a, b, c):
    return a* x **2 + b*x + c

y = func(np.arange(-4, 5, 0.1), 5, 10, -30)
# print(y)
# print('-------------------------')
# y = [5*i**2 + 10*i -30 for i in x]
# y = 5*np.arange(-10, 5)**2 - 10 * np.arange(-10, 5) - 30
# print(y)


# In[ ]:


# 4. промежутки возрастания и убывания


# In[155]:


plt.title = (f' корни функции = {solve(a, b, c)} ')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()

plt.plot(max_x, max_y, 'go', label = 'точка минимума')
plt.plot(negative_x, func (negative_x, 5, 10, -30), 'b', label = 'Убывание')
plt.plot(positive_x, func (positive_x, 5, 10, -30), 'r', label = 'Возрастание')
plt.legend()
plt.show


# In[ ]:




