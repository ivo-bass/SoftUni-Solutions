def get_negative(*args):
    return tuple(filter(lambda x: x < 0, args))


def get_positive(*args):
    return tuple(filter(lambda x: x >= 0, args))


def calc_total_sum(*args):
    return sum(args)


def compare(ps, ns):
    if ps > abs(ns):
        return 'The positives are stronger than the negatives'
    elif ps < abs(ns):
        return 'The negatives are stronger than the positives'


nums = tuple(map(int, input().split()))

negative = get_negative(*nums)
positive = get_positive(*nums)
n_sum = calc_total_sum(*negative)
p_sum = calc_total_sum(*positive)

print(n_sum)
print(p_sum)
print(compare(p_sum, n_sum))
