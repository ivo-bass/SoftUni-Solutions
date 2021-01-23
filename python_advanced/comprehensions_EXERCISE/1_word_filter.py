def get_input():
    return input().split()


def is_valid(el):
    return len(el) % 2 == 0


def filter_words(ll):
    return [w for w in ll if is_valid(w)]


def print_output(ll):
    [print(el) for el in ll]


word_list = get_input()
result = filter_words(word_list)
print_output(result)
