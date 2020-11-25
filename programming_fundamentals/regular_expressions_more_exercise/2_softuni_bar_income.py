import re

pattern = \
	r"^(%(?P<name>[A-Z][a-z]+)%).*(<(?P<product>\w+)>).*" \
	r"(\|(?P<count>\d+)\|)([^\d]*)((?P<price>\d+(\.\d+)?)\$)$"
total = 0

data = input()
while not data == "end of shift":
	match = re.match(pattern, data)
	if match:
		name, product = match.group("name"), match.group("product")
		cost = int(match.group("count")) * float(match.group("price"))
		print(f"{name}: {product} - {cost:.2f}")
		total += cost
	data = input()

print(f"Total income: {total:.2f}")
