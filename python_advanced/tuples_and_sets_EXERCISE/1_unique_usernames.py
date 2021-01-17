def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    the_input = set()
    for _ in range(count):
        text = input()
        the_input.add(text)
    return the_input


def print_elements_in_collection(collection):
    for el in collection:
        print(el)


n = int(input())
names_set = get_for_input(n)

print_elements_in_collection(names_set)
