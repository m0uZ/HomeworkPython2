# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите число: ')
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# i = 1
# result = 1
# print('[ ', end ='')
# while i <= number - 1:
#     result *= i
#     i += 1
#     print(result, end = ', ')
# print(result * number,']')

# Задайте список из n чисел последовательности (1+\frac 1 n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# import fractions
# number = int(input('Введите число: '))
# sum = 0
# sum1 = 0
# for i in range(1, number + 1):
#     sum += round((1 + 1/i)**i, 2)
#     sum1 += round((1 + float(fractions.Fraction(1, i))) ** i, 2)
# print(sum)
# print(sum1)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# from random import randint
# n = int(input("Введите размер списка: "))
# some_list = [ randint(-n,n) for _ in range(n) ]
# sum = 1
# print(some_list)
# with open ('num.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         sum *= some_list[int(line)]
# print(sum)

# Реализуйте алгоритм перемешивания списка.
# from random import randint
# n = int(input("Введите размер списка: "))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# for i in range(n // 2):
#     temp = some_list[i]
#     some_list[i] = some_list[i - 1]
#     some_list[i - 1] = temp
# print(some_list)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

# list1 = [1, 2, 3, 2, 0]
# list2 = [5, 1, 2, 7, 3, 2]
# list3 = []
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             list3.append(list1[i])
#             break
# print(list3)


