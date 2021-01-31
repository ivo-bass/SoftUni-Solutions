PATH = 'text.txt'
CHARS_TO_REPLACE = ("-", ",", ".", "!", "?")
REPLACEMENT = '@'


def replace_bad_chars(ll):
    replaced = []
    for l in ll:
        for ch in CHARS_TO_REPLACE:
            l = l.replace(ch, REPLACEMENT)
        replaced.append(l)
    return replaced


def get_even_lines(ll):
    return [ll[i].rstrip().split() for i in range(len(ll)) if i % 2 == 0]


def reverse_order(ll):
    return [line[::-1] for line in ll]


def print_output(ll):
    for line in ll:
        print(' '.join(line))


with open(PATH) as file:
    lines = file.readlines()
    replaced = replace_bad_chars(lines)
    even_lines = get_even_lines(replaced)
    reversed_lines = reverse_order(even_lines)

print_output(reversed_lines)
