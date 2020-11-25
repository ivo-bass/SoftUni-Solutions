from re import compile

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
data = '\n'.join(lines)
pattern = compile(r"\d+")
matches = pattern.findall(data)

print(*matches)
