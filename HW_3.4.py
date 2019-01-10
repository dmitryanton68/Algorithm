# 4. Определить, какое число в массиве встречается чаще всего.

a = list(map(int, input("Введите через пробелы массив чисел:  ").split(' ')))

i = 0
max_ = 0
max_num = 0

while i <= len(a) - 1:
    if max_ <= a.count(a[i]):
        max_ = a.count(a[i])
        max_num = a[i]
    i += 1

print(f'Число {max_num} встречается в массиве чаще всего - {max_} раз(а)')
