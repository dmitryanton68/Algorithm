# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = int(input('Введите число:  '))


def turnover(num, new_num):
    if len(str(num)) > 1:
        b = num % 10
    else:
        b = num
    new_num += b * 10 ** (len(str(num)) - 1)
    num = num // 10
    if num == 0:
        return new_num
    else:
        return turnover(num, new_num)


print(f'Было {a}, стало {turnover(a, 0)}')
