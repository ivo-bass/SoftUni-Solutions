def get_input():
    return input().split(', ')


def make_string(co, cap):
    return f'{co} -> {cap}'


countries = get_input()
capitals = get_input()
[print(make_string(countries[i], capitals[i])) for i in range(len(countries))]
