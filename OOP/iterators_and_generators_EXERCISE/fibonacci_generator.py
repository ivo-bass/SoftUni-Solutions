def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        nth = n1 + n2
        n1 = n2
        n2 = nth


generator = fibonacci()
for i in range(5):
    print(next(generator))
