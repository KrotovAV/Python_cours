
# n = 3

# print('')
# print('n =', n)

# # F−1 = 1,
# # F−2 = -1,
# # Fn = F(n+2)−F(n+1).
# # [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def fibo(a):
#     if a == -1:
#         return 1
#     if a == -2:
#         return -1
#     if a <- 2:
#         return fibo(a - 1) + fibo(a - 2)
#     #            -3 - 1  +     -3 - 2
#     #            -4      +     -5
#     #             -3     +      5
#     #               2
#     # return fibo(a + 2) + fibo(a + 1)
#     #           -3 + 2       -3 + 1
#     #           -1           -2
#     #               1       -1
#     #                   0

# for i in range(-n, 0):
#     print(i, '-', fibo(i))

def form_fibo_list_symmetrical(number):
number = abs(number)

# shared part for n = 1 [fib-1, fib0, fib1]:
fibo_list = [1, 0, 1]

# fill positive (common fibonacci) items:
# fib0 <- fibo_list[1], fib1 <- fibo_list[2]
for i in range(3, number+2):
fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

# fill negative (negofibonacci) items
for i in range(2, number+1):
fibo_list.insert(0, fibo_list[1] - fibo_list[0])

return fibo_list


print()