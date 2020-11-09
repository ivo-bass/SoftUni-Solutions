from math import ceil

guests = int(input())
budget = int(input())

cakes = ceil(guests / 3)
eggs = guests * 2

total_costs = cakes * 4 + eggs * 0.45
money_difference = budget - total_costs

if money_difference < 0:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(money_difference):.2f} lv. more.")
else:
    print(f"Lyubo bought {cakes} Easter bread and {eggs} eggs.")
    print(f"He has {money_difference:.2f} lv. left.")
