def squares(n):
    for i in range(1, n+1):
        yield i * i


# print(list(squares(5)))