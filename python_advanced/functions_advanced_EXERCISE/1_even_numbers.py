def filter_even_nums(*args):
    return filter(lambda x: x % 2 == 0, args)


numbers = map(int, input().split())

print(list(filter_even_nums(*numbers)))
