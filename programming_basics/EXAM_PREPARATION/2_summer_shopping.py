budget = int(input())
towel_price = float(input())
discount = int(input())

umbrella_price = 2/3 * towel_price
slippers_price = 75/100 * umbrella_price
bag_price = 1/3 * (towel_price + slippers_price)
price = towel_price + umbrella_price + slippers_price + bag_price
cost = price - (discount / 100 * price)

if budget >= float(cost):
    left = budget - float(cost)
    print(f"Annie's sum is {cost:.2f} lv. She has {left:.2f} lv. left.")
else:
    more = float(cost) - budget
    print(f"Annie's sum is {cost:.2f} lv. She needs {more:.2f} lv. more.")
