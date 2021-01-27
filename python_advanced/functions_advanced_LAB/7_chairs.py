def print_output(ll):
    print(*ll, sep=', ')


def combinations(ll, n, comb=[]):
    if len(comb) == n:
        print_output(comb)
        return
    for i in range(len(ll)):
        comb.append(ll[i])
        combinations(ll[i+1:], n, comb)
        comb.pop()


names = input().split(', ')
n = int(input())

combinations(names, n)
