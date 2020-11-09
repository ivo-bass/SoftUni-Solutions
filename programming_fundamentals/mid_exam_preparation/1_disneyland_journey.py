journey_cost = float(input())
number_of_months = int(input())
saved_money = 0

for month in range(1, number_of_months + 1):
	if not month == 1 and not month % 2 == 0:
		saved_money -= 0.16 * saved_money
	elif month % 4 == 0:
		saved_money += 0.25 * saved_money
	saved_money += 0.25 * journey_cost

money_left = saved_money - journey_cost
if money_left >= 0:
	print(f"Bravo! You can go to Disneyland and you will have {money_left:.2f}lv. for souvenirs.")
else:
	print(f"Sorry. You need {abs(money_left):.2f}lv. more.")
