def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    the_input = set()
    for _ in range(count):
        text = input()
        the_input.add(text)
    return the_input


def get_while_input(endword):
    """Takes input with no given range but with keyword.
    Returns list of the inputs."""
    the_input = set()
    while True:
        text = input()
        if text == endword:
            return the_input
        the_input.add(text)


def print_output(s):
    print(len(s))
    for i in s:
        print(i)


END_COMMAND = 'END'


def main():
    guests_count = int(input())
    guest_list = get_for_input(guests_count)
    guests_arrived = get_while_input(END_COMMAND)

    absent_guests = sorted(guest_list - guests_arrived)
    print_output(absent_guests)


if __name__ == '__main__':
    main()
