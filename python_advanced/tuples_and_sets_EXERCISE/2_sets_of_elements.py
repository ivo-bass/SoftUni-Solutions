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


n, m = input().split(' ')
n, m = int(n), int(m)

n_set = get_for_input(n)
m_set = get_for_input(m)

shared_elements = n_set.intersection(m_set)
if shared_elements:
    print_elements_in_collection(shared_elements)
