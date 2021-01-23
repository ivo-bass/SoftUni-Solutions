def read_input():
    return input().split(', ')


def dict_from_list(ll):
    return {el: ord(el) for el in ll}


ll = read_input()
dd = dict_from_list(ll)
print(dd)
