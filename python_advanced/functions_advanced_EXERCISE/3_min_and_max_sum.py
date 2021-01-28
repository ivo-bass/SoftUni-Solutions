def min_number(*args):
    return min(args)


def max_number(*args):
    return max(args)


def sum_number(*args):
    return sum(args)


def print_output(ll):
    print(f'The minimum number is {min_number(*ll)}')
    print(f'The maximum number is {max_number(*ll)}')
    print(f'The sum number is: {sum_number(*ll)}')


print_output(list(map(int, input().split())))
