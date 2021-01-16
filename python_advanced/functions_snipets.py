def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    the_input = []
    for _ in range(count):
        text = input()
        the_input.append(text)
    return the_input


def get_while_input(endword):
    """Takes input with no given range but with keyword.
    Returns list of the inputs."""
    the_input = []
    while True:
        text = input()
        if text == endword:
            return the_input
        the_input.append(text)


def print_elements_in_collection(collection):
    for el in collection:
        print(el)
