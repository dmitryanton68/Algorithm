# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

a = list(map(int, input("Введите через пробелы массив чисел:  ").split(' ')))

min_1 = min(a)
a.pop(a.index(min_1))
min_2 = min(a)

print(f'Наименьшие элементы - это {min_1} и {min_2}')
