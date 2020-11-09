def draw_battle_field(n_raws):
	"""You will be given a number n representing the number of rows of the field.
	On the next n lines you will receive each row of the field as a string with
	numbers separated by a space. Each number greater than zero represents a ship
	with a health equal to the number value."""
	field = []
	for row_num in range(n_raws):  # first row = 0
		raw_values_list = [int(value) for value in input().split()]  # list of integer values for current row
		field.append(raw_values_list)  # append list of values for columns in the raws_list - lists in list
	return field


def attack(field, i_raw, i_col, destroyed):
	"""Each time a square is being attacked, if there is a ship there
	(number greater than 0) you should reduce its value."""
	if not field[i_raw][i_col] == 0:  # if there is a ship in the spot
		field[i_raw][i_col] -= 1  # reduce it's value
		if field[i_raw][i_col] == 0:  # if the ship is destroyed
			destroyed += 1  # increase the count of destroyed ships
	return destroyed


def main():
	destroyed_ships = 0
	number_of_rows = int(input())
	battle_field = draw_battle_field(number_of_rows)
	all_attacks = input().split()
	for current_attack in all_attacks:  # current attack = "{str}-{str}"
		attack_indexes = current_attack.split("-")  # attack_indexes = ["str", "str"]
		raw_index = int(attack_indexes[0])
		column_index = int(attack_indexes[1])
		destroyed_ships = attack(battle_field, raw_index, column_index, destroyed_ships)
	print(destroyed_ships)


if __name__ == '__main__':
	main()
