days_count = int(input())
bakers_count = int(input())
cakes_count_per_baker = int(input())
waffles_count_per_baker = int(input())
pancakes_count_per_baker = int(input())

total_cakes = cakes_count_per_baker * bakers_count * days_count
total_waffles = waffles_count_per_baker * bakers_count * days_count
total_pancakes = pancakes_count_per_baker * bakers_count * days_count

cakes_money = total_cakes * 45.00
waffles_money = total_waffles * 5.80
pancakes_money = total_pancakes * 3.20

total_money = cakes_money + waffles_money + pancakes_money
costs = total_money / 8

earned = total_money - costs

print(f"{earned:.2f}")
