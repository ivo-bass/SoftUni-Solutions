budget = float(input())
season = input()
place = ''
price = 0
destination = ''
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        place = "Hotel"
        price = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        place = "Hotel"
        price = 0.8 * budget
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    price = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")
