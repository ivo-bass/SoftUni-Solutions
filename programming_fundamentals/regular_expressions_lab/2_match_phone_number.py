from re import finditer

data = input()
pattern = r"(^|\s)(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
numbers = finditer(pattern, data)
numbers = [p.group(0) for p in numbers]

print(", ".join(numbers))
