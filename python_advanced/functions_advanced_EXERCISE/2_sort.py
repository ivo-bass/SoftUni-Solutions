def sort_nums(*args):
    return sorted(args)


numbers = map(int, input().split())

print(sort_nums(*numbers))
