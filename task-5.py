from random import randrange

OUTPUT_FILE = 'task-5.output.txt'


def generate_file():
    with open(OUTPUT_FILE, 'w') as fh:
        fh.write(' '.join(map(str, [randrange(1, 1000) for _ in range(randrange(10, 25))])))


def read_file():
    with open(OUTPUT_FILE) as fh:
        numbers = fh.read().split()

    return list(map(int, numbers))


def main():
    generate_file()
    numbers = read_file()
    print(sum(numbers))


if __name__ == '__main__':
    main()
