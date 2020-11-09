movie_title = input()
hall_type = input()
tickets_sold = int(input())

prices = {
    "A Star Is Born": {"normal": 7.5, "luxury": 10.5, "ultra luxury": 13.5},
    "Bohemian Rhapsody": {"normal": 7.35, "luxury": 9.45, "ultra luxury": 12.75},
    "Green Book": {"normal": 8.15, "luxury": 10.25, "ultra luxury": 13.25},
    "The Favourite": {"normal": 8.75, "luxury": 11.55, "ultra luxury": 13.95}
}
income = prices[movie_title][hall_type] * tickets_sold
print(f"{movie_title} -> {income:.2f} lv.")
