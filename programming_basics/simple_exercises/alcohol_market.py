whisky_price = float(input())
beer_litres = float(input())
wine_litres = float(input())
brandy_liters = float(input())
whisky_litres = float(input())

brandy_price = whisky_price / 2
wine_price = brandy_price - 40/100 * brandy_price
beer_price = brandy_price - 80/100 * brandy_price

beer_costs = beer_litres * beer_price
wine_costs = wine_litres * wine_price
brandy_costs = brandy_liters * brandy_price
whisky_costs = whisky_litres * whisky_price

total_costs = beer_costs + wine_costs + brandy_costs + whisky_costs

print(f"{total_costs:.2f}")
