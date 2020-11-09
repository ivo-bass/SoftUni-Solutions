people_waiting = int(input())
current_state_input = input()

current_state_list = [int(i) for i in current_state_input.split(' ')]

for wagon_index in range(len(current_state_list)):
	for person in range(people_waiting):
		if current_state_list[wagon_index] < 4:
			current_state_list[wagon_index] += 1
			people_waiting -= 1
		else:
			break

if people_waiting == 0 and sum(current_state_list) < len(current_state_list)*4:
	print("The lift has empty spots!")
elif people_waiting > 0 and sum(current_state_list) == len(current_state_list)*4:
	print(f"There isn't enough space! {people_waiting} people_waiting in a queue!")
print(' '.join(map(str, current_state_list)))
