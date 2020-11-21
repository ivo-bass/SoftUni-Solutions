from itertools import cycle
KEYS = [int(n) for n in input().strip().split()]


def decrypt_line(text):
	decrypted = ""
	index = 0
	for key in cycle(KEYS):
		decrypted += chr(ord(text[index]) - key)
		index += 1
		if index == len(text):
			return decrypted


def get_info(msg):
	start_treasure, stop_treasure = [index for index, char in enumerate(msg) if char == "&"]
	start_coordinates, stop_coordinates = msg.index("<"), msg.index(">")
	return msg[start_treasure+1:stop_treasure], msg[start_coordinates+1:stop_coordinates]


line = input()
while not line == "find":
	message = decrypt_line(line)
	treasure, coordinates = get_info(message)
	print(f"Found {treasure} at {coordinates}")
	line = input()
