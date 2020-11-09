budget = float(input())
count = int(input())

total_price = 0
for _ in range(count):
    name = input()
    price = float(input())
    if name == "Thrones":
        price *= 0.5
    elif name == "Lucifer":
        price *= 0.6
    elif name == "Protector":
        price *= 0.7
    elif name == "TotalDrama":
        price *= 0.8
    elif name == "Area":
        price *= 0.9
    total_price += price

money_difference = budget - total_price
if money_difference >= 0:
    print(f"You bought all the series and left with {money_difference:.2f} lv.")
else:
    print(f"You need {abs(money_difference):.2f} lv. more to buy the series!")
