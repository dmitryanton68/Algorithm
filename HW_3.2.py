# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

arr = list(map(int, input("Введите через запятую массив чисел:  ").split(',')))

index_arr = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        index_arr.append(i)
    else:
        pass

print(*index_arr)