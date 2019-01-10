# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

print("Введите построчно поэлементно матрицу 3 х 3")
matrix = [[int(input()) for _ in range(3)] for _ in range(3)]

b = []
matrix_1 = zip(*matrix)

for line in matrix_1:
    b.append(min(line))

print(f'Максимальный элемент среди минимальных элементов столбцов = {max(b)}')
