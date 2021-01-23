def get_input():
    return input().split(', ')


def make_text(word):
    return f'{word} -> {len(word)}'


def get_result(ll):
    return [make_text(w) for w in ll]


def get_output(result):
    return ', '.join(result)


word_list = get_input()
result = get_result(word_list)
print(get_output(result))
