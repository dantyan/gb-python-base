with open('task-2.txt') as fh:
    lines = fh.readlines()

line_number = len(lines)

print(f'Total lines: {line_number}')

for i, line in enumerate(lines, 1):
    print(f'Line {i}, has {len(line.split())} worlds')
