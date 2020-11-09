baklava_price = float(input())
muffin_price = float(input())
stolen_quantity = float(input())
sweets_quantity = float(input())
biscuits_quantity = int(input())

stolen_price = 1.6 * baklava_price
sweets_price = 1.8 * muffin_price
biscuits_price = 7.5

total_sum = stolen_quantity * stolen_price + sweets_quantity * sweets_price + biscuits_quantity * biscuits_price

print(f"{total_sum:.2f}")
