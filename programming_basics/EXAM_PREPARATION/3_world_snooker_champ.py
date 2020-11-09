stage = input()
ticket_type = input()
ticket_count = int(input())
picture = input()

prices = {"Quarter final": {"Standard": 55.5, "Premium": 105.2, "VIP": 118.9},
          "Semi final": {"Standard": 75.88, "Premium": 125.22, "VIP": 300.4},
          "Final": {"Standard": 110.1, "Premium": 160.66, "VIP": 400}}

price = prices[stage][ticket_type] * ticket_count

if price > 4000:
    price *= 0.75
elif price > 2500:
    price *= 0.9
    if picture == "Y":
        price += (40 * ticket_count)
else:
    if picture == "Y":
        price += (40 * ticket_count)

print(f"{price:.2f}")
