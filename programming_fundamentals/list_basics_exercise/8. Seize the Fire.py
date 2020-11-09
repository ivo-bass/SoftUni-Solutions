"""Create a program that calculates the total_water that is
needed to put out a "fire cell", based on the given information
about its "fire level" and how much it gets affected by total_water."""

fires_input = input()
total_water = int(input())

fires_list = list(fires_input.split("#"))
total_effort = 0
total_fire = 0
cells = []


def check_validity(type_, value_):
	"""There is a range of fire for each of the fire types,
	and if a cell’s value is below or exceeds it, it is
	invalid and you don’t need to put it out"""
	valid_levels = {
		"High": 81 <= value_ <= 125,
		"Medium": 51 <= value_ <= 80,
		"Low": 1 <= value_ <= 50
	}
	if valid_levels[type_]:
		return True


for fire in fires_list:
	current_fire = fire.split(" = ")
	current_type = current_fire[0]
	current_value = int(current_fire[1])
	if check_validity(current_type, current_value):
		if current_value <= total_water:
			total_water -= current_value
			total_effort += 0.25 * current_value
			total_fire += current_value
			cells.append(current_value)

print("Cells:")
for cell in cells:
	print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
