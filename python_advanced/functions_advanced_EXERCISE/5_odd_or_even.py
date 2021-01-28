ODD_COMMAND = 'Odd'
EVEN_COMMAND = 'Even'


def get_input():
    command = input()
    sequence = list(map(int, input().split()))
    return command, sequence


def devide_odd_nums(*args):
    return filter(lambda x: x % 2 != 0, args)


def devide_even_nums(*args):
    return filter(lambda x: x % 2 == 0, args)


def calculate_result(ll, *args):
    return sum(args) * len(ll)


action, nums = get_input()
devided = []
if action == ODD_COMMAND:
    devided = devide_odd_nums(*nums)
elif action == EVEN_COMMAND:
    devided = devide_even_nums(*nums)
print(calculate_result(nums, *devided))
