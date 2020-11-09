rooms_count = int(input())

total_free_chairs = 0
is_enough = True
for room in range(1, rooms_count + 1):
	room_condition = input().split()
	chairs_count = len(room_condition[0])
	chairs_taken = int(room_condition[1])
	free_chairs = chairs_count - chairs_taken
	if free_chairs < 0:
		is_enough = False
		chairs_needed = abs(free_chairs)
		print(f"{chairs_needed} more chairs needed in room {room}")
	else:
		total_free_chairs += free_chairs

if is_enough:
	print(f"Game On, {total_free_chairs} free chairs left")
