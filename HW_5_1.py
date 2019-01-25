# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

a = int(input("Введите количество предприятий:  "))

Enterprise = namedtuple('Enterprise', 'name, income')
lst = []
total_income = 0
i = 1

while i <= a:
    company_name = input("Введите название предприятия: ")
    income = 0
    for j in range(4):
        income = int(input(f'Введите доход за {j + 1} кв.: '))
        income += income
    company = Enterprise(company_name, income)
    total_income += income
    lst.append(company)
    i += 1

mid_income = total_income / a
low_income_lst = []
high_income_lst = []

for i in range(a):
    if lst[i][1] <= mid_income:
        low_income_lst.append(lst[i][0])
    else:
        high_income_lst.append(lst[i][0])

if high_income_lst == []:
    high_income_lst.append('нет ни одного предприятия')

print('***' * 40)
print(f'Доход этих предприятий на уровне или ниже среднего: ', *low_income_lst)
print(f'Доход этих предприятий выше среднего: ', *high_income_lst)
