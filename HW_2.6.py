# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

def guess(r, number):

    n = int(input('Угадай целое число от 0 до 100:  '))

    if n == r and number >= 1:
        return 'BINGO'

    if n < r and number > 1:
        print('Нет, чуть побольше будет!')
        return guess(r, number - 1)
    elif n > r and number > 1:
        print('Нет, чуть поменьше будет!')
        return guess(r, number - 1)
    elif number == 1:
        return f'Увы, не угадал, число = {rand}'


rand = randint(0, 100)
print(guess(rand, 10))
