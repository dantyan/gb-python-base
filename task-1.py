with open('task-1.txt', 'w') as fh:
    while True:
        data = input()
        if not data:
            break
        fh.write(f'{data}\n')
