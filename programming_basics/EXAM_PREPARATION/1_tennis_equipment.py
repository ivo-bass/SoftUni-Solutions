from math import ceil, floor

rocket_price = float(input())
rocket_count = int(input())
sneakers_count = int(input())
sneakers_price = 1/6 * rocket_price
total = rocket_count * rocket_price + sneakers_count * sneakers_price
total += total * 0.2
novac_costs = 1/8 * total
sponsors_costs = 7/8 * total

print(f"Price to be paid by Djokovic {floor(novac_costs)}")
print(f"Price to be paid by sponsors {ceil(sponsors_costs)}")
