import gettext

ru = gettext.translation('base', localedir='./locales', languages=['ru'])
ru.install()
_ = ru.gettext

with open('task-4.txt') as fh:
    lines = fh.readlines()

with open('task-4.output.txt', 'w') as fh:
    for line in lines:
        world, number = line.split('-')
        world = world.strip()
        number = number.strip()
        fh.write(f'{_(world)} - {number}\n')
