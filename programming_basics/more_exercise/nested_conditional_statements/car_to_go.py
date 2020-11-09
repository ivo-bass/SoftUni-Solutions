budget = float(input())
season = input()

classes = {budget <= 100: "Economy class",
           100 < budget <= 500: "Compact class",
           budget > 500: "Luxury class"}

cars = {"Economy class": {"Summer": "Cabrio", "Winter": "Jeep"},
        "Compact class": {"Summer": "Cabrio", "Winter": "Jeep"},
        "Luxury class": {"Summer": "Jeep", "Winter": "Jeep"}}

prices = {"Economy class": {"Summer": 0.35 * budget,
                            "Winter": 0.65 * budget},
          "Compact class": {"Summer": 0.45 * budget,
                            "Winter": 0.8 * budget},
          "Luxury class": {"Summer": 0.9 * budget,
                           "Winter": 0.9 * budget}}

class_ = classes[True]
car = cars[class_][season]
price = prices[class_][season]

print(f"{class_}")
print(f"{car} - {price:.2f}")
