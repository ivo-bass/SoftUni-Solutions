EVEN_COMMAND = 'even'


def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    if command == EVEN_COMMAND:
        return list(filter(lambda x: x % 2 == 0, nums))
    return list(filter(lambda x: x % 2 != 0, nums))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
