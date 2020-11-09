chicken_count = int(input())
fish_count = int(input())
vegi_count = int(input())

chicken_costs = 10.35 * chicken_count
fish_costs = 12.40 * fish_count
vegi_costs = 8.15 * vegi_count

total = chicken_costs + fish_costs + vegi_costs
dessert_costs = 0.2 * total
delivery = 2.50
total += dessert_costs + delivery

print(f"Total: {total:.2f}")
