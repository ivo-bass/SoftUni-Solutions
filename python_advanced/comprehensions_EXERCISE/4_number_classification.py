def get_input():
    return [int(s) for s in input().split(', ')]


def get_positives(ll):
    return {'Positive': [n for n in ll if n >= 0]}


def get_negatives(ll):
    return {'Negative': [n for n in ll if n < 0]}


def get_evens(ll):
    return {'Even': [n for n in ll if n % 2 == 0]}


def get_odds(ll):
    return {'Odd': [n for n in ll if not n % 2 == 0]}


def fill_categories(nums):
    return [
        get_positives(nums),
        get_negatives(nums),
        get_evens(nums),
        get_odds(nums)
    ]


def print_string(key, value):
    print(f'{key}: {", ".join([str(n) for n in value])}')


def print_dict(dd):
    return [print_string(key, value) for key, value in dd.items()]


def print_results(ll):
    return [print_dict(dd) for dd in ll]


numbers = get_input()
results = fill_categories(numbers)
print_results(results)
