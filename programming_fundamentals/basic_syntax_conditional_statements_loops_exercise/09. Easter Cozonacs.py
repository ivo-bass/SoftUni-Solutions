budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk_1l = price_flour * 1.25

cozonac_price = price_flour + price_eggs + 0.25 * price_milk_1l
cozonacs_count = 0
colored_eggs_count = 0
while budget > cozonac_price:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs_count += 3
    if cozonacs_count % 3 == 0:
        lost_eggs = cozonacs_count - 2
        colored_eggs_count -= lost_eggs

print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:0.2f}BGN left.")
