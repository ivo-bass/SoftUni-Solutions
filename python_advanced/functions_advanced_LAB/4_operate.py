from functools import reduce

mapper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def operate(operator, *args):
    return reduce(mapper[operator], args)
