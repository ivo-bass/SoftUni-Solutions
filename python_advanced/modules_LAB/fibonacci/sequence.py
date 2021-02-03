seq = [0, 1]


def create_seq(n):
    global seq

    if n < 0:
        raise ValueError
    elif n == 0:
        seq = []
    elif n == 1:
        seq = [0]
    else:
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
    return seq


def locate(n):
    if n not in seq:
        return f'The number {n} is not in the sequence'
    i = seq.index(n)
    return f'The number - {n} is at index {i}'
