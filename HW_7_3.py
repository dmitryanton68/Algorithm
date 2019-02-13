# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

# в Телеграм говорилось о том, что нужно делать int-массив

from random import randint, choice

# m = int(input("Введите m - натуральное нечётное число, ~равное половине массива:  "))
m = 5
n = 2 * m + 1
lst_input = [randint(0, 49) for i in range(n)]
print(f'Исходный        массив =', *lst_input)
print(f'Отсортированный массив =', *sorted(lst_input))


def select(lst):
    if n <= 1:
        return lst
    else:
        number = choice(lst)
        less = [i for i in lst if i < number]
        more = [i for i in lst if i > number]
        equal = [number] * lst.count(number)

    if len(lst) >= 2:
        mid = len(lst) / 2
        if len(less) == mid:
            return select(less)
        elif len(less) < mid < len(less) + len(equal):
            return equal[0]
        elif len(less) > mid:
            return select(less)
        return select(more)
    else:
        return lst[0]


print(f'Медиана = ', select(lst_input))
