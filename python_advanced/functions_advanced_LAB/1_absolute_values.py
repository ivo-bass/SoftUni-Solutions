def text_to_iterable(string):
    return map(float, string.split())


def list_of_abs(iter):
    return list(map(abs, iter))


text = input()
print(list_of_abs(text_to_iterable(text)))
