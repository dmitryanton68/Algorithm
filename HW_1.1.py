# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

N = int(input())

a1 = N % 10
a2 = (N % 100 - a1) // 10
a3 = N // 100

print(f'Sum of numbers = {a1 + a2 + a3}')
print(f'Multiplication of numbers = {a1 * a2 * a3}')
