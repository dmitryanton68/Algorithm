# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

a = list(map(float, input("Введите через пробелы массив чисел, содержащий отрицательные числа:  ").split(' ')))

b = []
i = 0

while i <= len(a) - 1:
    if a[i] < 0:
        b.append(a[i])
    i += 1

max_num = max(b)
max_ = a.index(max_num) + 1

print(f'Максимальный отрицательный элемент {max_num} стоит в последовательности на {max_} месте')
