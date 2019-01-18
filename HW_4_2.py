# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать (1) скорость и (2) сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

print('Вариант №1')

N = int(input('Номер простого числа:  '))

import cProfile

def search(N):
    a = [2, 3]
    if N == 1:
        return 2
    elif N == 2:
        return 3
    else:
        k = 4
        while len(a) < N:
            for i in a:
                if k % i == 0:
                    k += 1
                    break
            else:
                if k not in a:
                    a.append(k)
                    k += 1

        return a[N - 1]

cProfile.run('search(100)')

print(f'За нумером {N} значится число {search(N)}')
#
# ==================================================================
#
print('Вариант №2')

N = int(input('Номер простого числа:  '))

import cProfile

def seave(N):
    n = N * 10
    a = list(range(2, n))
    for i in a:
        a = list(filter(lambda x: (x == i) or not (x % i == 0), a))
    return a[N - 1]

cProfile.run('seave(100)')

print(f'За нумером {N} значится число {seave(N)}')
#
# =================================================================
# RESULT of timeit function work:
# =================================================================
# По Варианту №1:
# 100 loops, best of 3: 389 usec per loop - N = 100
# 100 loops, best of 3: 1.37 msec per loop - N = 200
# 100 loops, best of 3: 3.01 msec per loop - N = 300
# 100 loops, best of 3: 5.45 msec per loop - N = 400
# 100 loops, best of 3: 8.4 msec per loop - N = 500
# --- addition:
# 100 loops, best of 3: 33.7 msec per loop - N = 1000
# 100 loops, best of 3: 133 msec per loop - N = 2000
# 100 loops, best of 3: 298 msec per loop - N = 3000
# ==================================================================
# По Варианту №2:
# 100 loops, best of 3: 26.4 msec per loop - N = 100
# 100 loops, best of 3: 116 msec per loop - N = 200
# 100 loops, best of 3: 203 msec per loop - N = 300
# 100 loops, best of 3: 354 msec per loop - N = 400
# 100 loops, best of 3: 534 msec per loop - N = 500
# ==================================================================
# ВЫВОД:
# Время работы из расчёта на 1 номер искомого числа растёт линейно.
# Скорость работы Варианта №1 в среднем примерно в 70 раз выше, чем Варианта №2.
# Время обработки квадратично зависит от номера числа, что хорошо видно в Варианте №1
# (Вариант №2 на числах свыше N = 500 работает очень медленно) -> сложность О(n^2)
#
# =================================================================
# RESULT of cProfile function work:
# =================================================================
# По Варианту №1:
# cProfile.run('search(100)')
#
#         641 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 HW_4_2.py:13(search)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       539    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        98    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# ===============================================================================================
# По Варианту №2:
# cProfile.run('seave(100)')
#
#         169898 function calls in 0.056 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.055    0.055 <string>:1(<module>)
#         1    0.028    0.028    0.055    0.055 HW_4_2.py:45(seave)
#    169894    0.028    0.000    0.028    0.000 HW_4_2.py:49(<lambda>)
#         1    0.000    0.000    0.056    0.056 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===================================================================================================
# ВЫВОД:
# При одном и том же номере искомого числа код Варианта №2 сделал в 256 раз больше вызовов, чем код Варианта №1,
# причём 84% вызовов Варианта №1 пришлось на встроенный метод len(), скорость работы которого относительно высока.
# В Варианте №2 практически все вызовы пришлись на lambda функцию, которая и заняла основное время работы кода.
#