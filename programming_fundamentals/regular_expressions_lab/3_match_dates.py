from re import finditer

data = input()
pattern = r"\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b"
dates = finditer(pattern, data)

for date in dates:
	print(f"Day: {date.group(1)}, Month: {date.group(3)}, Year: {date.group(4)}")
