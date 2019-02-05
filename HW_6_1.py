# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Python3.7, 64-bit
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
# Вариант №1
#
# from random import randint

# def min_max_swap(n):
#     i = 0
#     a = []
#
#     while i <= n - 1:
#         a.append(randint(0, 1000))
#         i += 1
#
#     j = 0
#     min_ = a[0]
#     while j <= n - 1:
#         if a[j] < min_:
#             min_ = a[j]
#         j += 1
#     i_min = a.index(min_)
#
#     k = 0
#     max_ = a[0]
#     while k <= n - 1:
#         if a[k] > max_:
#             max_ = a[k]
#         k += 1
#     i_max = a.index(max_)
#
#     a[i_min] = max_
#     a[i_max] = min_
#
#     return a
#
#
#
# n = int(input("Введите длину массива случайных целых чисел:  "))
# print(f'Массив после  замены  = ', *min_max_swap(n))
#
# ==========================================================================
#  Размер памяти, выделяемый под переменные = 364.
#  ==========================================================================
#
# Вариант № 2
#
# from random import randint
#
# def min_max_swap(n):
#     i = 0
#     a = []
#
#     while i <= n - 1:
#         a.append(randint(0, 1000))
#         i += 1
#
#     min_ = min(a)
#     i_min = a.index(min_)
#     max_ = max(a)
#     i_max = a.index(max_)
#     a[i_min] = max_
#     a[i_max] = min_
#
#     return a
#
#
# n = int(input("Введите длину массива случайных целых чисел:  "))
# print(f'Массив после  замены  = ', *min_max_swap(n))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Размер памяти, выделяемый под переменные = 364.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
#
# def ascii_letters(start, finish):
#     if start == finish:
#         return str((f'{start} -> {chr(start)}'))
#
#     if start < finish:
#         return (str((f'{start} -> {chr(start)}')) + ', ' + str(ascii_letters(start + 1, finish)))
#     else:
#         return ''
#
# s = 32
# f = 127
#
# ii = (f - s + 9) // 10
# s_i = s
#
#
# for i in range(0, ii):
#     if s_i + 10 <= f:
#         f_i = s_i + 10
#     else:
#         f_i = f
#     print(ascii_letters(s_i, f_i))
#     s_i = f_i + 1
#     i += 1
#
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Размер памяти, выделяемый под переменные = 440.
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
#
#
def sign():
    s1 = input('Введите знак операции:  ')

    if s1 == '0' or s1 == '+' or s1 == '-' or s1 == '*' or s1 == '/':
        return s1
    else:
        return sign()


def second_num(sec_num):
    print('ALARM: деление на 0')
    sec_num = float(input('Введите новое значение второго числа:  '))
    if sec_num == 0:
        return second_num(sec_num)
    else:
        return sec_num


while True:

    a = float(input('Введите первое число:  '))
    b = float(input('Введите второе число:  '))
    i = sign()

    if i == '/' and b == 0:
        b = second_num(b)

    if i == '+':
        print(f'a + b = {a + b}')
    elif i == '-':
        print(f'a - b = {a - b}')
    elif i == '*':
        print(f'a * b = {a * b}')
    elif i == '/':
        print(f'a / b = {a / b}')
    elif i == '0':
        print(f'Вычисления завершены')
        break
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Размер памяти, выделяемый под переменные = 506.
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Подсчёт по переменным из задач к урокам:

from HW_6_1_1 import summarizing

print(summarizing(locals()))
