from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x * y, args)
