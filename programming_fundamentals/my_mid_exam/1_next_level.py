needed_exp = float(input())
count_of_battles = int(input())

for battle in range(1, count_of_battles + 1):
	exp_per_battle = float(input())

	if battle % 3 == 0:
		exp_per_battle *= 1.15
	elif battle % 5 == 0:
		exp_per_battle *= 0.9
	elif battle % 15 == 0:
		exp_per_battle *= 0.05

	needed_exp -= exp_per_battle

	if needed_exp <= 0:
		print(f"Player successfully collected his needed experience for {battle} battles.")
		break

if needed_exp > 0:
	print(f"Player was not able to collect the needed experience, {needed_exp:.2f} more needed.")
