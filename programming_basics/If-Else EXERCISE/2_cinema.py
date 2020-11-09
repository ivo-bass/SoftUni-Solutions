projection_type = input()
rows = int(input())
columns = int(input())

projections_prices = {'Premiere': 12.00, 'Normal': 7.50, 'Discount': 5.00}

income = rows * columns * projections_prices[projection_type]

print(f"{income:.2f}")
