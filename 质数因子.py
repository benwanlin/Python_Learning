# import math
# while True:
#     try:
#
#         def is_prime(number):
#             if number == 1:
#                 return False
#             if number == 2:
#                 return True
#             for i in range(2, int(math.sqrt(number)) + 1):
#                 if number % i == 0:
#                     return False
#             return True
#
#         def func(number):
#             if is_prime(number):
#                 return [number]
#             res = []
#             for i in range(2, number):
#                 if is_prime(i):
#                     remainder = 0
#                     while remainder == 0:
#                         factor, remainder = divmod(number, i)
#                         if remainder == 0:
#                             res.append(i)
#                             number = factor
#                             if is_prime(number):
#                                 res.append(number)
#                                 return res
#
#         num = int(input())
#         res = func(num)
#         for i in res:
#             print(i, end=' ')
#
#     except:
#         break

a, res = int(input()), []
for i in range(2, a // 2 + 1):
    while a % i == 0:
        a = a / i
        res.append(i)
print(" ".join(map(str, res)) + " " if res else str(a) + " ")