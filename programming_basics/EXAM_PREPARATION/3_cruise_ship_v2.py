prices = {"Mediterranean": {    "standard cabin": 27.5,
                            "cabin with balcony": 30.2,
                                     "apartment": 40.5},
          "Adriatic": {    "standard cabin": 22.99,
                       "cabin with balcony": 25,
                                "apartment": 34.99},
          "Aegean": {    "standard cabin": 23,
                     "cabin with balcony": 26.6,
                              "apartment": 39.8}}


def cost(cruise, cabin, days):
    cost = prices[cruise][cabin] * 4 * days
    if days > 7:
        cost *= 0.75
    return cost


def main():
    cruise = input()
    cabin = input()
    days = int(input())
    costs = cost(cruise, cabin, days)
    print(f"Annie's holiday in the {cruise} sea costs {costs:.2f} lv.")


if __name__ == "__main__":
    main()
