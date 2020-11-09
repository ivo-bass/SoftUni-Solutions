budget = float(input())
destination = input()
season = input()
days_count = int(input())

day_price = {"Dubai": {"Summer": 40000, "Winter": 45000},
             "Sofia": {"Summer": 12500, "Winter": 17000},
             "London": {"Summer": 20250, "Winter": 24000}}

total_price = days_count * day_price[destination][season]
if destination == "Dubai":
    total_price *= 0.7
if destination == "Sofia":
    total_price *= 1.25

money_difference = budget - total_price
if money_difference >= 0:
    print(f"The budget for the movie is enough! We have {money_difference:.2f} leva left!")
else:
    print(f"The director needs {abs(money_difference):.2f} leva more!")
