# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib
from random import choices, shuffle
from string import ascii_lowercase

N = int(input("Введите количество знаков в строке:  "))
S = ''.join(choices(ascii_lowercase, k=N))
print(f'Строка S = "{S}"')


def form_stack(st):
    full_stack = []
    for i in range(len(st)):
        for j in range(len(st)):
            if st[i:j + 1] not in full_stack and st[i:j + 1] != '':
                full_stack.append(st[i:j + 1])
    return full_stack


def rabin_karpa(s, subs):
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return 1
    return 0


full_stack = form_stack(S)

for _ in range(N ** 2):
    next_S = str(shuffle(list(S)))
    for i in form_stack(next_S):
        if i not in full_stack and i != '':
            full_stack.append(i)

calculation = 0
for sub in full_stack:
    calculation += rabin_karpa(S, sub)

print(f'Количество подстрок, подсчитанных прямо = {len((form_stack(S)))}.')
print(f'Количество подстрок, полученных в результате перемешивания исходной строки = {len(full_stack)}')
print(f'В строке S = "{S}" находится {calculation} уникальных подстрок, подсчитанных с использованием хэш-функций.')
