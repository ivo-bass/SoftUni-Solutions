def add_stop(li, i, s):
	if i in range(len(li)):
		li = li[:i] + s + li[i:]
	return li


def remove_stop(li, start_i, end_i):
	if start_i in range(len(li)) and end_i in range(len(li)):
		li = li[:start_i] + li[end_i+1:]
	return li


def switch(li, old, new):
	if old in li:
		li = li.replace(old, new)
	return li


stops = input()

while True:
	data = input()
	if data == "Travel":
		print(f"Ready for world tour! Planned stops: {stops}")
		break
	command, token1, token2 = data.split(":")
	if command == "Add Stop":
		index = int(token1)
		stops = add_stop(stops, index, token2)
	elif command == "Remove Stop":
		start,  end = int(token1), int(token2)
		stops = remove_stop(stops, start, end)
	elif command == "Switch":
		stops = switch(stops, token1, token2)
	print(stops)
