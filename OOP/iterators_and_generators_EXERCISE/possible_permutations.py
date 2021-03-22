def possible_permutations(ll):
    if len(ll) <= 1:
        yield ll
    else:
        for i in range(len(ll)):
            for p in possible_permutations(ll[:i] + ll[i + 1:]):
                yield [ll[i]] + p


# [print(n) for n in possible_permutations([1, 2, 3])]
