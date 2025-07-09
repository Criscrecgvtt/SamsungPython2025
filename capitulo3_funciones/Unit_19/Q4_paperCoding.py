from functools import reduce

n = reduce(lambda x, y: x + y, range(1,101))
print(n)
