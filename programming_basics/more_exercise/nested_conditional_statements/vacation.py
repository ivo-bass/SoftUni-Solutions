budget = float(input())
season = input()

places = {budget <= 1000: "Camp",
          1000 < budget <= 3000: "Hut",
          budget > 3000: "Hotel"}

locations = {"Summer": "Alaska", "Winter": "Morocco"}

prices = {"Camp": {"Summer": 0.65 * budget, "Winter": 0.45 * budget},
          "Hut": {"Summer": 0.8 * budget, "Winter": 0.6 * budget},
          "Hotel": {"Summer": 0.9 * budget, "Winter": 0.9 * budget}}

place = places[True]
location = locations[season]
price = prices[place][season]

print(f"{location} - {place} - {price:.2f}")
