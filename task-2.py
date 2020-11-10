seconds = input('Enter number of seconds: ')

if not seconds.isdigit():
    print('Only numbers allowed')
    exit()

seconds = int(seconds)

minutes, sec = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

print('{:d}:{:02d}:{:02d}'.format(hours, minutes, sec))
