budget = float(input())
category = input()
people_count = int(input())

prices = {"VIP": 499.99, "Normal": 249.99}

transport_price = {1 <= people_count <= 4: 0.75 * budget,
                   5 <= people_count <= 9: 0.6 * budget,
                   10 <= people_count <= 24: 0.5 * budget,
                   25 <= people_count <= 49: 0.4 * budget,
                   people_count >= 50: 0.25 * budget}

money_left = budget - transport_price[True]
price = prices[category] * people_count
difference = money_left - price

if difference >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")
