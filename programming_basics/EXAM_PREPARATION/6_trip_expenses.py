holiday_days = int(input())
limit = 60

for _ in range(holiday_days):
    total_costs = 0
    items_bought = 0
    money_left = 0
    while True:
        command = input()
        money_left = limit - total_costs

        if command == "Day over":
            print(f"Money left from today: {money_left:.2f}. You've bought {items_bought} products.")
            limit += money_left
            break

        curr_price = float(command)
        if curr_price > money_left:
            continue

        total_costs += curr_price
        items_bought += 1

        if total_costs == limit:
            print(f"Daily limit exceeded! You've bought {items_bought} products.")
            limit = 60
            break
