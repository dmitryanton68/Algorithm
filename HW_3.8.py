# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print("Введите построчно поэлементно матрицу 4 х 4")
matrix = [[int(input()) for _ in range(4)] for _ in range(4)]

for line in matrix:
    line.append(sum(line))
    for i, j in enumerate(line):
        print(f'{j:>5}', end=' ')
    print('')

# альтернативные варианты вывода (плохо форматированные):
# print(*line)
# print(f'{str(line):>5}', end=' ')
# print("{:>5}".format(str(line)))
# print(' '.join(map(str, line)))

# max_len = max([len(str(e)) for r in a for e in r])
# for row in a:
#     print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))

# sum_column = [0]*len(matrix[0])
# print(sum_column)
#
# for line in matrix:
#     sum_line = 0
#     for i, item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#         print(f'{item:>5}', end=' ')
#     print(f' | {sum_line}')
