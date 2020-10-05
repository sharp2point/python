

revenue = int(input('Введите выручку вашей фирмы (целое число):'))
expense = int(input('Введите издержки вашей фирмы (целое число):'))
profit = revenue-expense
workers = 0
profit_for_worker = 0

if profit > 0:
    print(f'Доход вашей фирмы положителен: +{profit}')
elif profit < 0:
    print(f'Доход вашей фирмы отрицателен: {profit}')
else:
    print(f'Ваш доход: 0')
if profit != 0:
    workers = int(input('Введите колличество сотрудников фирмы:'))

    profit_for_worker = profit/workers

    if profit_for_worker > 0:
        print('Выручка фирмы на одного сотрудника: %.2f' % (profit_for_worker))
    elif profit_for_worker < 0:
        print(f'Фирма понесла издержки на одного сотрудника: %.2f' % (profit_for_worker))
    else:
        print(f'Выручка : 0')


