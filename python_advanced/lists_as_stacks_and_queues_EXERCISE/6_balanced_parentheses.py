sequence = input()

o_stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
}

success = True
for el in sequence:
    if el in pairs.values():
        o_stack.append(el)
    elif el in pairs.keys():
        if not o_stack:
            success = False
            break
        opening = o_stack.pop()
        if not opening == pairs[el]:
            success = False
            break

if success:
    print('YES')
else:
    print('NO')
