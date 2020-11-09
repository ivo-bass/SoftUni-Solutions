"""Create a program that calculates the profit after
buying some items and selling them on a higher price. """

items_input = input()
budget = float(input())

items_list = list(items_input.split("|"))
new_prices = []
profit = 0
current_budget = budget


def check_price(name, price):
	"""If a price for a certain item is higher
	than the maximum price, don’t buy it."""
	maximum_prices = {
		"Clothes": price <= 50,
		"Shoes": price <= 35,
		"Accessories": price <= 20.5
	}
	if maximum_prices[name]:
		return True


for item in items_list:
	item_split = list(item.split("->"))
	item_name = item_split[0]
	item_price = float(item_split[1])
	if check_price(item_name, item_price):
		if current_budget >= item_price:
			current_budget -= item_price
			new_prices.append(item_price * 1.4)
			profit += 0.4 * item_price

total_money = profit + budget
new_prices_formatted = [f'{p:.2f}' for p in new_prices]
print(*new_prices_formatted)
print(f"Profit: {profit:.2f}")
if total_money >= 150:
	print("Hello, France!")
else:
	print("Time to go.")
