products = {}
data = input()
while not data == "buy":
	name, price, quantity = data.split()
	if name not in products.keys():
		products[name] = {"price": float(price), "quantity": int(quantity)}
	else:
		products[name]["price"] = float(price)
		products[name]["quantity"] += int(quantity)
	data = input()

for name, x in products.items():
	total_price = x["price"] * x["quantity"]
	print(f"{name} -> {total_price:.2f}")
