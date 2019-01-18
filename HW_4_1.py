# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
print('Вариант №1')

import cProfile

from random import randint


def min_max_swap(n):
    i = 0
    a = []

    while i <= n - 1:
        a.append(randint(0, 1000))
        i += 1

    j = 0
    min_ = a[0]
    while j <= n - 1:
        if a[j] < min_:
            min_ = a[j]
        j += 1
    i_min = a.index(min_)

    k = 0
    max_ = a[0]
    while k <= n - 1:
        if a[k] > max_:
            max_ = a[k]
        k += 1
    i_max = a.index(max_)

    a[i_min] = max_
    a[i_max] = min_

    return a


cProfile.run('min_max_swap(1000)')

n = int(input("Введите длину массива случайных целых чисел:  "))
print(f'Массив после  замены  = ', *min_max_swap(n))

# ==========================================================================

print('Вариант № 2')

from random import randint

import cProfile

def min_max_swap(n):
    i = 0
    a = []

    while i <= n - 1:
        a.append(randint(0, 1000))
        i += 1

    min_ = min(a)
    i_min = a.index(min_)
    max_ = max(a)
    i_max = a.index(max_)
    a[i_min] = max_
    a[i_max] = min_

    return a

cProfile.run('min_max_swap(1000)')

n = int(input("Введите длину массива случайных целых чисел:  "))
print(f'Массив после  замены  = ', *min_max_swap(n))

# ==========================================================================
# RESULT of timeit function work:
# ==========================================================================
# По Варианту №1:
# 100 loops, best of 3: 16.5 usec per loop - n = 10
# 100 loops, best of 3: 71.1 usec per loop - n = 50
# 100 loops, best of 3: 144 usec per loop - n = 100
# 100 loops, best of 3: 753 usec per loop - n = 500
# 100 loops, best of 3: 1.53 msec per loop - n = 1000
# ==========================================================================
# По Варианту №2:
# 100 loops, best of 3: 13.4 usec per loop - n = 10
# 100 loops, best of 3: 65.5 usec per loop - n = 50
# 100 loops, best of 3: 127 usec per loop - n = 100
# 100 loops, best of 3: 657 usec per loop - n = 500
# 100 loops, best of 3: 1.32 msec per loop - n = 1000
# ==========================================================================
# ВЫВОД:
# Время обработки на 1 число в последовательности колеблется около среднего значения.
# Среднее значение в варианте №1 = 1.51 мксек, в варианте №2 = 1,31 мксек.
# Вариант со встроенными функциями (№2) тратит в среднем на 13% времени меньше.
# Время обработки линейно зависит от количества членов последовательности -> сложность О(n)
#
# ==========================================================================
# RESULT of cProfile function work (cProfile.run('min_max_swap(1000)')):
# ==========================================================================
# По Варианту №1:
#
#          6031 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.001    0.001    0.004    0.004 HW_4_1.py:10(min_max_swap)
#      1000    0.001    0.000    0.002    0.000 random.py:173(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:217(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1025    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
# ==========================================================================
# По Варианту №2:
#
#          6037 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.001    0.001    0.003    0.003 HW_4_1.py:53(min_max_swap)
#      1000    0.001    0.000    0.002    0.000 random.py:173(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:217(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1029    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
# ========================================================================================
# ВЫВОД: в Варианте №1 вызовов чуть меньше, чем в Варианте №2, а время работы больше =>
# => скорость Варианта №1 ниже(скорость уже была оценена в ВЫВОДЕ по итогам работы timeit)