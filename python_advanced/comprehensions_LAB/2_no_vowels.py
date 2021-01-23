VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS.update({ch.upper() for ch in VOWELS})


def is_valid(char):
    return char not in VOWELS


def remove_vowels(text):
    return [el for el in text if is_valid(el)]


def print_output(ll):
    print(''.join(ll))


text = input()
ll = remove_vowels(text)
print_output(ll)
