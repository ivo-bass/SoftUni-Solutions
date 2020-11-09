width_space = int(input())
length_space = int(input())
height_space = int(input())

total_space = width_space * length_space * height_space
free_space = total_space
is_done = False
while free_space > 0:
    command = input()
    if command == "Done":
        is_done = True
        break
    count = int(command)
    free_space -= count

if is_done:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
