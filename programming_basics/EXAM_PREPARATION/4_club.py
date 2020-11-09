profit_target = float(input())
club_income = 0
money_needed = profit_target

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {money_needed:.2f} leva more.")
        break

    cocktail_count = int(input())
    cocktail_price = len(cocktail_name)
    order_price = cocktail_count * cocktail_price

    if order_price % 2 > 0:
        discount = 0.25 * order_price
    else:
        discount = 0

    final_price = order_price - discount
    club_income += final_price

    if club_income >= profit_target:
        print("Target acquired.")
        break
    else:
        money_needed = profit_target - club_income

print(f"Club income - {club_income:.2f} leva.")
