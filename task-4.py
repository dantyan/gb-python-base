number = input('Enter number: ')

if not number.isdigit():
    print('Only numbers allowed')
    exit()

_max = 0
a = int(number)
while a > 0:
    b = a % 10
    _max = max(_max, b)
    a = a // 10

print(f'Max number is: {_max}')

print(' ------------------------------ ')

# Другой вариант решения
print('Max number is:', max(map(int, list(number))))
