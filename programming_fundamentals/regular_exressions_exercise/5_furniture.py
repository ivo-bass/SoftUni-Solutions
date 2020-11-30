from re import compile

regex = r">>(?P<name>\w+)<<(?P<price>[0-9]+(\.[0-9]+)?)!(?P<quantity>[0-9]+)"
pattern = compile(regex)
furniture = {}

while True:
	data = input()
	if data == "Purchase":
		break
	order = pattern.match(data)
	if order:
		furniture[order.group("name")] = float(order.group("price")) * int(order.group("quantity"))

print("Bought furniture:")
for item in furniture.keys():
	print(item)
print(f"Total money spend: {sum(furniture.values()):.2f}")
