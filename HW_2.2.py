# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Введите натуральное число:  '))
c = a

even_num = 0
odd_num = 0


def even_odd(num, j, k):
    if len(str(num)) > 1:
        b = num % 10
    else:
        b = num
    if b % 2 == 0:
        j += 1
    else:
        k += 1
    num = num // 10
    if num == 0:
        return j, k
    else:
        return even_odd(num, j, k)


print(f'В числе {c} содержится: '
      f'{even_odd(a, even_num, odd_num)[1]} нечётных и {even_odd(a, even_num, odd_num)[0]} чётных цифр.')

# a = int(input('Введите натуральное число:  '))
# c = a
#
# i = 0
# even_num = 0
# odd_num = 0
# length = len(str(a))
#
# while i < length:
#     if len(str(a)) > 1:
#         b = a % 10
#     else:
#         b = a
#     if b % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1
#     a = a // 10
#     i += 1
#
# print(f'В числе {c} содержится {odd_num} нечётных и {even_num} чётных цифр.')
