def text_to_iterable(string):
    return map(float, string.split())


def list_of_rounded(iter):
    return list(map(round, iter))


text = input()
print(list_of_rounded(text_to_iterable(text)))
