def solution():
    def integers():
        temp = 1
        while True:
            yield temp
            temp += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        res = []
        for i in seq:
            if n == len(res):
                return res
            res.append(i)

    return (take, halves, integers)


# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))