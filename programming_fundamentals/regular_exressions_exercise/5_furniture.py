from re import compile

regex = r">>(?P<name>\w+)<<(?P<price>[0-9]+(\.[0-9]+)?)!(?P<quantity>[0-9]+)"
pattern = compile(regex)

all_items = []
total_money = 0
data = input()
while not data == "Purchase":
	order = pattern.findall(data)
	if order:
		name = order[0][0]
		price = float(order[0][1])
		quantity = int(order[0][3])
		total_money += price * quantity
		all_items.append(name)
	data = input()

print("Bought furniture:")
for item in all_items:
	print(item)
print(f"Total money spend: {total_money:.2f}")
