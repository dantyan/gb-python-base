number = input('Enter number: ')

if not number.isdigit():
    print('Only numbers allowed')
    exit()

n_1, n_2, n_3 = int(number), int(number*2), int(number*3)

answer = n_1 + n_2 + n_3
print(f'Answer is: {answer}')


