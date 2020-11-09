flowers_type = input()
flowers_count = int(input())
budget = int(input())

flowers_prices = {"Roses": 5, "Dahlias": 3.8, "Tulips": 2.8,
                  "Narcissus": 3, "Gladiolus": 2.5}
costs = flowers_prices[flowers_type] * flowers_count

if flowers_type == "Roses" and flowers_count > 80:
    costs *= 0.9
elif flowers_type == "Dahlias" and flowers_count > 90:
    costs *= 0.85
if flowers_type == "Tulips" and flowers_count > 80:
    costs *= 0.85
if flowers_type == "Narcissus" and flowers_count < 120:
    costs *= 1.15
if flowers_type == "Gladiolus" and flowers_count < 80:
    costs *= 1.2

money_difference = budget - costs

if money_difference < 0:
    print(f"Not enough money, you need {abs(money_difference):.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_difference:.2f} leva left.")
