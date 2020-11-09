party_size = int(input())
days = int(input())

earnings = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5

    earnings += 50
    earnings -= 2 * party_size

    if day % 3 == 0:
        earnings -= 3 * party_size
    if day % 5 == 0:
        earnings += 20 * party_size
        if day % 3 == 0:
            earnings -= 2 * party_size

coins_per_companion = earnings // party_size

print(f"{party_size} companions received {coins_per_companion} coins each.")
