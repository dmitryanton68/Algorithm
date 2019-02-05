# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

n = int(input("Введите длину массива случайных целых чисел:  "))

i = 0
a = []

while i <= n - 1:
    a.append(randint(0, 1000))
    i += 1

print(f'Первоначальный массив = ', *a)

min_ = min(a)
i_min = a.index(min_)
max_ = max(a)
i_max = a.index(max_)
a[i_min] = max_
a[i_max] = min_

print(f'Массив после  замены  = ', *a)

# Попытка сделать swap провалилась. Почему нельзя сделать min(a), max(a) = max(a), min(a) ?