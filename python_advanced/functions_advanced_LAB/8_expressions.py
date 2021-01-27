def make_expressions(ll, expression='', currant_sum=0):
    if not ll:
        return [(expression, currant_sum)]
    plus_exp = make_expressions(
        ll[1:], expression=f'{expression}+{ll[0]}', currant_sum=currant_sum+ll[0])
    minus_exp = make_expressions(
        ll[1:], expression=f'{expression}-{ll[0]}', currant_sum=currant_sum-ll[0])

    return plus_exp + minus_exp


data = list(map(int, input().split(', ')))
# data = [1, 1, 1, 1]
# all_expressions = make_expressions(data)

[print(f'{exp}={res}') for exp, res in make_expressions(data)]
