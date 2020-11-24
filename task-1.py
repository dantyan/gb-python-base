from sys import argv

_, hours, rate, bonus = argv

print('-' * 60)
print(f'{"hours:":>12} {hours}')
print(f'{"rate:":>12} {rate}')
print(f'{"bonus:":>12} {bonus}')
print('=' * 60)
print(f'{"result:":>12} {int(hours) * int(rate) + int(bonus)}')
print('-' * 60)
