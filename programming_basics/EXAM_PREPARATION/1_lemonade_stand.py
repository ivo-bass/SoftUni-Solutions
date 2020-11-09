lemons = float(input())
sugar = float(input())
water = float(input())

lemon_juice = lemons * 980
water_ml = 1000 * water
sugar_add = 30/100 * sugar

lemonade = lemon_juice + water_ml + sugar_add
cups_sold = int(lemonade / 150)
earnings = format(float(cups_sold) * 1.20, '.2f')

print("All cups eggs_sold:", cups_sold)
print("Money earned:", earnings)
