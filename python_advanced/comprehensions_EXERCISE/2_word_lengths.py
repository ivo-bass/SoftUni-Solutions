def get_input():
    return input().split(', ')


def make_text(word):
    return f'{word} -> {len(word)}'


def get_result(ll):
    return [make_text(w) for w in ll]


word_list = get_input()
result = get_result(word_list)
print(*result, sep=', ')
