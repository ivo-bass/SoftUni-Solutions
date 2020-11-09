def check_validity(type_, value_):
	valid_levels = {
		"High": 81 <= value_ <= 125,
		"Medium": 51 <= value_ <= 80,
		"Low": 1 <= value_ <= 50
	}
	if valid_levels[type_]:
		return True


fires_input = input().split("#")
total_water = int(input())

total_effort = 0
total_fire = 0
cells = []


for fire in fires_input:
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
