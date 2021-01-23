DIVISORS_RANGE = range(2, 11)


def get_range(s, e):
    return range(s, e+1)


def is_valid(n):
    return any(n % i == 0 for i in DIVISORS_RANGE)


def filter_nums(given_range):
    return [num for num in given_range if is_valid(num)]


given_range = get_range(int(input()), int(input()))
result = filter_nums(given_range)
print(result)
