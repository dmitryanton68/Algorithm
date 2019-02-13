# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint

# в Телеграм говорилось о том, что нужно делать int-массив
n = 11
lst = [randint(0, 49) for i in range(n)]
print(f'Исходный массив = ', *lst)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def sorting(lst):
    if len(lst) < 2:
        return lst
    md = int(len(lst) / 2)
    left = sorting(lst[:md])
    right = sorting(lst[md:])
    return merge(left, right)


print(f'Отсортированный массив = ', *sorting(lst))
