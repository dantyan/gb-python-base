a = 2
b = 10

if a >= b:
    print('wrong data')

i = 1
print(f'{i}-й день: {a}')
while a < b:
    a += a * 0.1
    i += 1
    print(f'{i}-й день: {a:.2f}')

print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.')
