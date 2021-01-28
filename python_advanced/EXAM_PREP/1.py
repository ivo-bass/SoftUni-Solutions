from collections import deque


def get_input():
    males = list(map(int, input().split()))
    females = deque(map(int, input().split()))
    return males, females


def match(f, m, count):
    f.popleft()
    m.pop()
    count += 1
    return f, m, count


def unmatch(f, m, c):
    f.popleft()
    m[-1] -= 2
    return f, m, c


def check_for_0s(f, m):
    found = False
    if f[0] <= 0:
        found = True
        f.popleft()
    if m[-1] <= 0:
        found = True
        m.pop()
    return f, m, found


def check_for_25s(f, m):
    found = False
    if f[0] % 25 == 0:
        found = True
        f.popleft()
        # Проверявам дали има още елементи в листа след първия pop()
        if f:
            f.popleft()
    if m[-1] % 25 == 0:
        found = True
        m.pop()
        if m:
            m.pop()
    return f, m, found


def check_for_match(f, m, count):
    current_female = f[0]
    current_male = m[-1]
    if current_female == current_male:
        return match(f, m, count)
    return unmatch(f, m, count)


def print_output(f, m, count):
    m_str = 'none'
    f_str = 'none'

    if m:
        m = m[::-1]
        m_str = ', '.join(map(str, m))
    if f:
        f_str = ', '.join(map(str, f))

    print(f'Matches: {count}')
    print(f'Males left: {m_str}')
    print(f'Females left: {f_str}')


def main():
    males, females = get_input()
    matches = 0

    while males and females:
        females, males, is_found = check_for_0s(females, males)
        # Ако намери нула, трябва да завърти наново цикъла, за да провери пак следващите елементи
        if is_found:
            continue
        females, males, is_found = check_for_25s(females, males)
        # Ако намери делимо на 25, трябва да завърти наново цикъла, за да провери пак следващите елементи
        if is_found:
            continue
        females, males, matches = check_for_match(females, males, matches)

    print_output(females, males, matches)


main()
