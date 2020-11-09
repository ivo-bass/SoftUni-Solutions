days_of_trip = int(input())
budget = float(input())
people_count = int(input())
fuel_price = float(input())
food_per_person_per_day = float(input())
room_per_person_per_day = float(input())

is_enough = True
current_expenses = 0
food_expenses = food_per_person_per_day * people_count * days_of_trip
current_expenses += food_expenses

hotel_expenses = people_count * room_per_person_per_day * days_of_trip
if people_count > 10:
	hotel_expenses *= 0.75
current_expenses += hotel_expenses

for day in range(1, days_of_trip + 1):
	travelled_distance = float(input())
	travel_expenses = travelled_distance * fuel_price
	current_expenses += travel_expenses

	if day % 3 == 0 or day % 5 == 0:
		current_expenses += 0.4 * current_expenses

	if day % 7 == 0:
		current_expenses -= current_expenses / people_count

	if current_expenses > budget:
		print(f"Not enough money to continue the trip. You need {current_expenses - budget:.2f}$ more.")
		is_enough = False
		break

if is_enough:
	print(f"You have reached the destination. You have {budget - current_expenses:.2f}$ budget left.")
