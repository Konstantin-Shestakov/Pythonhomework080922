from random import randint


# # 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.

# # Пример:

# #  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# #

# # n = [2, 3, 5, 9, 3] 
# # Ist = []
# # for i in range(1, len(n), 2):
# #    Ist.append(n[i])
# # print(f'{n} -> на не четных позициях {Ist} Ответ: {sum([n[i] for i in range(1, len(n), 2)])}')

# #   2. Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:

# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]
# # 
# # 

# n = [2, 3, 4, 5, 6]
# def mul(i):
#     return n[i] * n[(i+1)*-1]

# def zero(arr):
#     lst =[]
#     for i in range(len(n)//2):
#         lst.append(mul(i))
#     return lst

# def not_zero(arr):
#     lst =[]
#     for i in range((len(n)//2)+1):
#         lst.append(mul(i))
#     return lst

# print((not_zero(n), zero(n))[len(n) %2 == 0]) 

# #   3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# # максимальным и минимальным значением дробной части элементов.

# # Пример:

# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# def decimals(arr):
#     return [arr[i] % 1 for i in range(len(arr))]
    
# n = [1.1, 1.2, 3.1, 5, 10.01]

# print(int((max(decimals(n)) - min(decimals(n))) * 100) / 100)


# # ______________________________________________________________________________________________________________________________

#   4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = 45

# def binary(n):
#     b = ''
#     while n>0:
#         b= str(n%2) + b
#         n = n//2
#     return int(b)

# print(binary(n))
#
# ______________________________________________________________________________________________________________________________



# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]




# def fibb(n):
#     lst = []
#     f1, f2 = 1, 1
#     for i in range(abs(n)):
#         lst.append(f1)
#         f1, f2 = f2, f1 + f2
#     return lst
# start_time = datetime.now()        
# def neg_fibb(n):
#     lst = []
#     f1, f2 = 1, -1
#     for i in range(abs(n)):
#         lst.append(f1)
#         f1, f2 = f2, (f1 + 1) - (f2 + 1)
#     return lst
# print(f'Вариант 1: отработал за {datetime.now() - start_time}')

# start_time2 = datetime.now()  
# def neg_fibb_2(n):
#     lst = fibb(n)
#     for i in range(len(lst)):
#         if i %2 != 0:
#             lst[i] = lst[i]*(-1)
#     lst1 = lst[::-1]
#     return lst1
# print(f'Вариант 2: отработал за {datetime.now() - start_time2}')    
# n = 10


# print(neg_fibb(n)[::-1] + [0] + fibb(n))

# print(neg_fibb_2(n) + [0] + fibb(n))




# ______________________________________________________________________________________________________________________________
# 6.
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| 
# элементов вправо,# если K – положительное и влево, если отрицательное.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N, во второй строке записаны N целых чисел Ai,
# а в последней – целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.

# IN
# 5
# 5 3 7 4 6
# 3
# OUT
# 7 4 6 5 3


# ______________________________________________________________________________________________________________________________


# k = 3
# lst = [5, 3, 7, 4, 6]
# def ShiftElements(lst, K):
#     index = 0
#     lst_2 = []
#     for i in range(len(lst)):
#         if K > 0:
#             if i + len(lst) - abs(K) < len(lst):
#                 lst_2.append(lst[i + len(lst) - abs(K)])
#             else:
#                 lst_2.append(lst[index])
#                 index += 1
#         else:
#             if i + abs(K) < len(lst):
#                 lst_2.append(lst[i + abs(K)])
#             else:
#                 lst_2.append(lst[index])
#                 index += 1
#     return lst_2
                
# print(ShiftElements(lst, k))



# def shift(lst, steps):
#     if steps < 0:
#         for i in range(abs(steps)):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
# nums = [5, 3, 7, 4, 6]
# print(nums)
 
# shift(nums, -2)
# print(nums)
 
# shift(nums, 3)
# print(nums)









# # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from functools import reduce

# def mul(a, b):
#      return a * b
    
# def f_string(n):
#      return reduce(mul, [i for i in range(1, n + 1)])
    
# def result(n):
#      return "*".join([str(i) for i in range(1, n + 1)])
  

# try:
#     N = int(input('число? '))
#     print('(' + ", ".join([result(i) for i in range(1, N + 1)]) + ') ' + '->', [f_string(i) for i in range(1, N + 1)])
# except:
#     print('Введите число')


  


