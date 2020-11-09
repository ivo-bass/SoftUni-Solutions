budget = float(input())
extras_count = int(input())
costume_price = float(input())

if extras_count > 150:
    costume_costs = costume_price * 0.9 * extras_count
else:
    costume_costs = costume_price * extras_count

decor_costs = 0.1 * budget
total_costs = costume_costs + decor_costs
money_difference = budget - total_costs

if money_difference < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_difference):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_difference:.2f} leva left.")
