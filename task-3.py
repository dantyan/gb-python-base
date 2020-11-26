def main():
    filename = 'task-3.txt'
    with open(filename) as fh:
        lines = fh.readlines()

    less_users = []
    salaries = []
    print('-' * 24)
    for line in lines:
        name, salary = line.split()
        name = name.strip()
        salary = float(salary)
        if salary < 20_000:
            less_users.append(name)
        salaries.append(salary)
        print(f'{name:>16}: {salary}')
    print('-' * 24)

    print('Users with salary less than 20 000:')
    for name in less_users:
        print(f'{name}')
    print('-' * 24)
    print(f'Avg salary: {sum(salaries) / len(salaries):.2f}')
    print('-' * 24)


if __name__ == '__main__':
    main()
