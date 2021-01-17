def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    the_input = set()
    for _ in range(count):
        line = input().split()
        for el in line:
            the_input.add(el)
    return the_input


def print_elements_in_collection(collection):
    for el in collection:
        print(el)


n = int(input())
periodic_table = get_for_input(n)
print_elements_in_collection(periodic_table)
