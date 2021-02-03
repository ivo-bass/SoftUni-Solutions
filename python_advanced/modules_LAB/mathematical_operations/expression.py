from .operations import devide, multiply, subtract, add, power


MAPPER = {
    '/': devide,
    '*': multiply,
    '-': subtract,
    '+': add,
    '^': power,
}


def calc_expression(expr):
    x, sign, y = expr.split()
    x = float(x)
    y = int(y)
    if MAPPER[sign]:
        return f'{MAPPER[sign](x, y):.2f}'
