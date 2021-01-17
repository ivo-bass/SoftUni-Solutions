def get_for_input(count):
    the_input = []
    for _ in range(count):
        text = input()
        the_input.append(text)
    return the_input


def generate_intersections(ll):
    intersections = []
    for el in ll:
        first_range, second_range = el.split('-')
        f_x, f_y = first_range.split(',')
        f_x, f_y = int(f_x), int(f_y)
        first_set = set()
        for num in range(f_x, f_y+1):
            first_set.add(num)
        s_x, s_y = second_range.split(',')
        s_x, s_y = int(s_x), int(s_y)
        second_set = set()
        for num in range(s_x, s_y+1):
            second_set.add(num)
        intersection = first_set.intersection(second_set)
        intersections.append(intersection)
    return intersections


def find_longest_set(ll):
    longest_set = set()
    for a_set in ll:
        if len(a_set) > len(longest_set):
            longest_set = a_set.copy()
    return longest_set


n = int(input())
ranges_list = get_for_input(n)
intersections = generate_intersections(ranges_list)
longest = list(find_longest_set(intersections))
print(f'Longest intersection is {longest} with length {len(longest)}')
