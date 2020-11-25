from re import findall

data = input()
regex = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
names = findall(regex, data)

print(" ".join(names))
