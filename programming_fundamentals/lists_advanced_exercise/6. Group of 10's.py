list_of_numbers = [int(s) for s in input().split(", ")]

group = 0

while list_of_numbers:
	group += 10
	current_group_items = list(filter(lambda x: x <= group, list_of_numbers))
	for item in current_group_items:
		list_of_numbers.remove(item)
	print(f"Group of {group}'s: {current_group_items}")
