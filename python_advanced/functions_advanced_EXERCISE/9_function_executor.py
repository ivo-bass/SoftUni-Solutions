def func_executor(*args):
    return [get_result(tup[0], tup[1]) for tup in args]


def get_result(func, args):
    return func(*args)
