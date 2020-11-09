days_of_adventure = int(input())
count_of_players = int(input())
all_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())

water_needed = days_of_adventure * count_of_players * water_per_person_per_day
food_needed = days_of_adventure * count_of_players * food_per_person_per_day
finish = True

for day in range(1, days_of_adventure + 1):
	energy_loss = float(input())
	all_energy -= energy_loss

	if all_energy <= 0:
		finish = False
		print(f"You will run out of energy. You will be left with {food_needed:.2f} food and {water_needed:.2f} water.")
		break

	if day % 2 == 0:
		all_energy *= 1.05
		water_needed *= 0.7

	if day % 3 == 0:
		all_energy *= 1.1
		food_needed -= food_needed / count_of_players

if finish:
	print(f"You are ready for the quest. You will be left with - {all_energy:.2f} energy!")
