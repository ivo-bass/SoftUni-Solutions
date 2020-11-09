cruise = input()
cabin = input()
days = int(input())

prices = {"Mediterranean": {"standard cabin": 27.5,
                            "cabin with balcony": 30.2,
                            "apartment": 40.5},
          "Adriatic": {"standard cabin": 22.99,
                       "cabin with balcony": 25,
                       "apartment": 34.99},
          "Aegean": {"standard cabin": 23,
                     "cabin with balcony": 26.6,
                     "apartment": 39.8}}

cost = prices[cruise][cabin] * 4 * days

if days > 7:
    cost *= 0.75

print(f"Annie's holiday in the {cruise} sea costs {cost:.2f} lv.")
