def print_result(ll):
    print(''.join(ll))


def permutation(_list, current_index=0):
    if current_index == len(_list):
        print_result(_list)
        return
    for i in range(current_index, len(_list)):
        _list[i], _list[current_index] = _list[current_index], _list[i]
        permutation(_list, current_index+1)
        _list[i], _list[current_index] = _list[current_index], _list[i]


string_list = list(input())
permutation(string_list)
