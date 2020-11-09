# With FOR cycle will be better

allowed_quantity = int(input())
days_left = int(input())

christmas_spirit = 0
current_day = 0
total_costs = 0

ornament_price = 2
skirt_price = 5
garlands_price = 3
lights_price = 15

while days_left > 0:
    current_day += 1
    days_left -= 1
    if current_day % 11 == 0:
        allowed_quantity += 2
    if current_day % 2 == 0:
        total_costs += ornament_price * allowed_quantity
        christmas_spirit += 5
    if current_day % 3 == 0:
        total_costs += skirt_price * allowed_quantity + garlands_price * allowed_quantity
        christmas_spirit += 13
    if current_day % 5 == 0:
        total_costs += lights_price * allowed_quantity
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        total_costs += skirt_price + garlands_price + lights_price
        if days_left == 0:
            christmas_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")