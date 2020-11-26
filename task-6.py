import re
from pprint import pprint


def clean_hours(hours):
    ret = re.sub(r'\D', '', hours)
    if ret:
        return int(ret)

    return 0


def main():
    with open('task-6.txt') as fh:
        lines = fh.readlines()

    ret = {}
    for line in lines:
        lesson, pairs = line.split(':')
        lesson = lesson.strip()
        hours = pairs.split()
        ret[lesson] = sum(map(clean_hours, hours))

    pprint(ret)


if __name__ == '__main__':
    main()
