def jump(li, le, pos):
	pos = pos + le
	if pos > len(li) - 1:
		pos = 0
	if li[pos] == 0:
		print(f"Place {pos} already had Valentine's day.")
	else:
		li[pos] -= 2
		if li[pos] <= 0:
			li[pos] = 0
			print(f"Place {pos} has Valentine's day.")
	return li, pos


def end(li, pos):
	print(f"Cupid's last position was {pos}.")
	failed_count = len(li) - li.count(0)
	if li.count(0) == len(li):
		print("Mission was successful.")
	else:
		print(f"Cupid has failed {failed_count} places.")


neighbourhood = [int(s) for s in input().split("@")]
position = 0
while True:
	command = input().split()
	if command[0] == "Love!":
		end(neighbourhood, position)
		break
	elif command[0] == "Jump":
		length = int(command[1])
		neighbourhood, position = jump(neighbourhood, length, position)

