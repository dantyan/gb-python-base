from functools import reduce
print(reduce(lambda prev, el: prev + el, [i for i in range(100, 1000, 2)]))

