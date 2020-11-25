from re import compile

data = input()
pattern = compile(r"\b_([A-Za-z0-9]+)\b")
matches = pattern.findall(data)

print(",".join(matches))
