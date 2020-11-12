print('Добро пожаловать')

income = input('Выручка: ')
outcome = input('Издержки: ')

income = int(income)
outcome = int(outcome)

lucky_year = False
if income > outcome:
    print('Удачный год вы в плюсе =)')
    lucky_year = True
else:
    print('Печально но вы в минусе')

if lucky_year:
    print(f'{income/outcome:.2f} сотношение прибыли к затратам')
    workers = input('Укажите число работников: ')
    workers = int(workers)
    print(f'{income/workers:.2f} Прибыль из расчета на работника')
