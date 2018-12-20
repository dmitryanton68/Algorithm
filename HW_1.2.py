# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

num_five = 101
num_six = 110

print(f'Five = {num_five}')
print(f'Six = {num_six}')

f1 = num_five % 10
f2 = (num_five % 100 - f1) // 10
f3 = num_five // 100

s1 = num_six % 10
s2 = (num_six % 100 - s1) // 10
s3 = num_six // 100

if f1 == 1 and s1 == 1:
    log_and_1 = 1
else:
    log_and_1 = 0

if f2 == 1 and s2 == 1:
    log_and_2 = 1
else:
    log_and_2 = 0

if f3 == 1 and s3 == 1:
    log_and_3 = 1
else:
    log_and_3 = 0

print(f'Result of logical "AND" = {log_and_3}{log_and_2}{log_and_1}.')
print(f'Truth table')
print(f' A  B  A AND B')
print(f' 1  1     1')
print(f' 1  0     0')
print(f' 0  1     0')
print(f' 0  0     0')

if f1 == 1 or s1 == 1:
    log_or_1 = 1
else:
    log_or_1 = 0

if f2 == 1 or s2 == 1:
    log_or_2 = 1
else:
    log_or_2 = 0

if f3 == 1 or s3 == 1:
    log_or_3 = 1
else:
    log_or_3 = 0

print(f'Result of logical "OR" = {log_or_3}{log_or_2}{log_or_1}.')
print(f'Truth table')
print(f' A  B  A OR B')
print(f' 1  1    1')
print(f' 1  0    1')
print(f' 0  1    1')
print(f' 0  0    0')

if (f1 == 1 and s1 == 0) or (f1 == 0 and s1 == 1):
    log_xor_1 = 1
else:
    log_xor_1 = 0

if (f2 == 1 and s2 == 0) or (f2 == 0 and s2 == 1):
    log_xor_2 = 1
else:
    log_xor_2 = 0

if (f3 == 1 and s3 == 0) or (f3 == 0 and s3 == 1):
    log_xor_3 = 1
else:
    log_xor_3 = 0

print(f'Result of logical "EXCLUSIVE OR" = {log_xor_3}{log_xor_2}{log_xor_1}.')
print(f'Truth table')
print(f' A  B  A XOR B')
print(f' 1  1     0')
print(f' 1  0     1')
print(f' 0  1     1')
print(f' 0  0     0')

if f1 == 1:
    log_not_f_1 = 0
else:
    log_not_f_1 = 1

if f2 == 1:
    log_not_f_2 = 0
else:
    log_not_f_2 = 1

if f3 == 1:
    log_not_f_3 = 0
else:
    log_not_f_3 = 1

if s1 == 1:
    log_not_s_1 = 0
else:
    log_not_s_1 = 1

if s2 == 1:
    log_not_s_2 = 0
else:
    log_not_s_2 = 1

if s3 == 1:
    log_not_s_3 = 0
else:
    log_not_s_3 = 1

print(f'Result of logical "NOT" of number 5 = {log_not_f_3}{log_not_f_2}{log_not_f_1}.')
print(f'Result of logical "NOT" of number 6 = {log_not_s_3}{log_not_s_2}{log_not_s_1}.')
print(f'Truth table')
print(f' A  ~A')
print(f' 1   0')
print(f' 0   1')

print(f'Result of bitwise left shift of number 5 (<<2) = {num_five}{0}{0} (it equals 20).')
print(f'Result of bitwise right shift of number 5 (>>2) = {f3} (it equals 1).')

print(f'Right shift on one position equals dividing by two, left shift - multiplying by two.')
