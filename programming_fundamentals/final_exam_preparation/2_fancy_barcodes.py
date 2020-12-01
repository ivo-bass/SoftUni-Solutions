from re import findall


def find_group(word):
	result = ""
	for char in word:
		if char.isdigit():
			result += char
	if result:
		return result
	return "00"


regex = r"^(@#+)([A-Z][A-Za-z0-9]*[A-Z])(@#+)$"
count = int(input())
for _ in range(count):
	barcode = input()
	match = findall(regex, barcode)
	if match:
		text = match[0][1]
		if len(text) >= 6:
			group = find_group(text)
			print(f"Product group: {group}")
			continue
	print("Invalid barcode")
