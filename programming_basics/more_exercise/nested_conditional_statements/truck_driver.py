season = input()
mileage_per_month = float(input())

rates = {mileage_per_month <= 5000: {"Spring": 0.75,
                                     "Autumn": 0.75,
                                     "Summer": 0.9,
                                     "Winter": 1.05},
         5000 < mileage_per_month <= 10000: {"Spring": 0.95,
                                             "Autumn": 0.95,
                                             "Summer": 1.10,
                                             "Winter": 1.25},
         10000 < mileage_per_month <= 20000: {"Spring": 1.45,
                                              "Autumn": 1.45,
                                              "Summer": 1.45,
                                              "Winter": 1.45}}

rate = rates[True][season]
earned = rate * mileage_per_month * 4
earned *= 0.9

print(f"{earned:.2f}")
