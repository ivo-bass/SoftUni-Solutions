from re import compile

data = input()
compiled_pattern = compile(r"(^|(?<=\s))(-?\d+(\.\d+)?)($|(?=\s))")
matches = compiled_pattern.findall(data)
numbers = [match[1] for match in matches]

print(*numbers)
