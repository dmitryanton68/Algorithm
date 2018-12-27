# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def ascii_letters(start, finish):
    if start == finish:
        return str((f'{start} -> {chr(start)}'))

    if start < finish:
        return (str((f'{start} -> {chr(start)}')) + ', ' + str(ascii_letters(start + 1, finish)))
    else:
        return ''

s = 32
f = 127

ii = (f - s + 9) // 10
s_i = s

for i in range(0, ii):
    if s_i + 10 <= f:
        f_i = s_i + 10
    else:
        f_i = f
    print(ascii_letters(s_i, f_i))
    s_i = f_i + 1
    i += 1
