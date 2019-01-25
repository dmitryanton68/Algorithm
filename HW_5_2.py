# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
import copy

a = deque(input("Введите в 16-ной системе первое число:  "))
b = deque(input("Введите в 16-ной системе второе число:  "))

a_copy = copy.deepcopy(a)
b_copy = copy.deepcopy(b)


def rule_of_sum(x, y, add=0):
    num_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    z = num_hex.index(x) + num_hex.index(y) + add
    if z < 16:
        return (0, num_hex[z])
    else:
        return (1, num_hex[z - 16])


num_a = len(a)
num_b = len(b)
m = max(num_a, num_b)


def summarizing(a, b, m):
    num_a = len(a)
    num_b = len(b)
    m = max(num_a, num_b)
    if m - num_a == 0:
        n = m - num_b
        for k in range(n):
            b.appendleft('0')
    else:
        n = m - num_a
        for k in range(n):
            a.appendleft('0')
    summ = deque([])
    for i in range(m - 1, -1, -1):
        if i == m - 1:
            c = rule_of_sum(a[i], b[i])[1]
        else:
            c = rule_of_sum(a[i], b[i], rule_of_sum(a[i + 1], b[i + 1])[0])[1]
        summ.appendleft(c)
    return summ


print(f'Сумма 16-ных чисел: ', *a_copy, ' + ', *b_copy, ' = ', *summarizing(a, b, m))


def rule_of_mult(x, y, add=0):
    num_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    z = num_hex.index(x) * num_hex.index(y) + add
    if z < 16:
        return (0, num_hex[z])
    else:
        return (z // 16, num_hex[z % 16])


mult = deque([])
result_mult = []

for i in range(m - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            c = rule_of_mult(a[j], b[i])[1]
        else:
            c = rule_of_mult(a[j], b[i], rule_of_mult(a[j + 1], b[i])[0])[1]
        mult.appendleft(c)
    if rule_of_mult(a[0], b[i])[0] != 0:
        mult.appendleft(str(rule_of_mult(a[0], b[i])[0]))
    result_mult.append(copy.deepcopy(mult))
    mult.clear()


def addition_right(result_mult):
    for i in range(1, len(result_mult)):
        for j in range(i):
            g = result_mult[i]
            g.append('0')
            result_mult[i] = g
            g = []
    return result_mult


result_mult = addition_right(result_mult)


def addition_left(result_mult, max_len):
    for i in range(0, len(result_mult)):
        if max_len > len(result_mult[i]):
            for _ in range(max_len - len(result_mult[i])):
                h = result_mult[i]
                h.appendleft('0')
                result_mult[i] = h
                h = []
    return result_mult


if len(result_mult) == 1:
    result = result_mult
else:
    max_len = 0
    for i in range(0, len(result_mult)):
        if max_len < len(result_mult[i]):
            max_len = len(result_mult[i])

    result_mult = addition_left(result_mult, max_len)
    result = deque(['0' for i in range(max_len)])

    for i in range(0, len(result_mult)):
        result = summarizing(result, result_mult[i], max_len)
        if len(result) > max_len:
            max_len = len(result)
        result_mult = addition_left(result_mult, max_len)

print(f'Произведение 16-ных чисел: ', *a_copy, ' + ', *b_copy, ' = ', *result)
