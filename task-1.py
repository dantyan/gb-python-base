from datetime import date

today = date.today()

_str = input('Введите произвольную строку: ')
print(f'спасибо, вы ввели: {_str}, длина строки - {len(_str)} сим.')

year = input('Enter your year of birth(ex: 1980): ')
print(f'You entered {year}')
i_year = int(year)

if i_year > today.year:
    print('you entered incorrect year')
else:
    age = today.year - i_year
    print(f'You are {age} years old')
