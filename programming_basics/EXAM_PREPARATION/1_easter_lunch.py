count_cakes = int(input())
count_eggs_cartons = int(input())
cookies_kg = int(input())

price_cakes = count_cakes * 3.2
price_eggs = count_eggs_cartons * 4.35
price_cookies = cookies_kg * 5.40
price_paint = count_eggs_cartons * 12 * 0.15

total = price_cakes + price_cookies + price_eggs + price_paint

print(f"{total:.2f}")
