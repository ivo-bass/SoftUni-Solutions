budget = float(input())
gas_litres = float(input())
day = input()

gas_price = 2.10 * gas_litres
guide_price = 100
total = gas_price + guide_price
if day == 'Saturday':
    total *= 0.9
elif day == 'Sunday':
    total *= 0.8

money_difference = budget - total
if money_difference < 0:
    print(f"Not enough money! Money needed: {abs(money_difference):.2f} lv.")
else:
    print(f"Safari time! Money left: {money_difference:.2f} lv. ")
