# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

a = list(map(int, input("Введите через пробелы массив чисел:  ").split(' ')))

min_ = min(a)
max_ = max(a)
i_min = a.index(min_)
i_max = a.index(max_)
summ = 0

if i_min < i_max:
    for i in range(i_min + 1, i_max):
        summ += a[i]
else:
    for i in range(i_max + 1, i_min):
        summ += a[i]

print(f'Сумма элементов между min и max = {summ}')
