count = int(input())

highest_rating = 0
best_movie = ''
lowest_rating = 10
worst_movie = ''
all_ratings = 0
for _ in range(count):
    name = input()
    rating = float(input())
    if rating > highest_rating:
        highest_rating = rating
        best_movie = name
    if rating < lowest_rating:
        lowest_rating = rating
        worst_movie = name
    all_ratings += rating

avrg_rating = all_ratings / count

print(f"{best_movie} is with highest rating: {highest_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {avrg_rating:.1f}")
