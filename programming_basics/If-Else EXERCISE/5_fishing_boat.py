budget = int(input())
season = input()
fishermen_count = int(input())

rent_price = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, 'Winter': 2600}
price = rent_price[season]

if fishermen_count <= 6:
    price *= 0.9
elif 7 <= fishermen_count <= 11:
    price *= 0.85
elif fishermen_count >= 12:
    price *= 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    price *= 0.95

money_difference = budget - price

if money_difference < 0:
    print(f"Not enough money! You need {abs(money_difference):.2f} leva.")
else:
    print(f"Yes! You have {money_difference:.2f} leva left.")
