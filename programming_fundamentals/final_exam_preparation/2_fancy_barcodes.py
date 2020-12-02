from re import match, findall

regex = r"^(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)$"
count = int(input())
for _ in range(count):
	barcode = input()
	if match(regex, barcode):
		group = findall(r"\d", barcode)
		if group:
			print(f"Product group: {''.join(group)}")
		else:
			print(f"Product group: 00")
	print("Invalid barcode")
