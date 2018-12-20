# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы в алфавите:   '))

if num > (ord('z') - ord('a') + 1):
    num = int(input('В алфавите всего 26 букв, введите заново:  '))
    if num > (ord('z') - ord('a') + 1):
        print('На выход!')
        pass
    else:
        letter = chr(num + ord('a') - 1)
else:
    letter = chr(num + ord('a') - 1)

print(f'Буква N{num} - это "{letter}"')
