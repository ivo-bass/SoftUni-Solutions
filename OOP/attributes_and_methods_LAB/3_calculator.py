class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for n in args:
            res *= n
        return res

    @staticmethod
    def divide(*args):
        res = None
        for i, n in enumerate(args):
            if i == 0:
                res = n
            else:
                res /= n
        return res

    @staticmethod
    def subtract(*args):
        res = None
        for i, n in enumerate(args):
            if i == 0:
                res = n
            else:
                res -= n
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
