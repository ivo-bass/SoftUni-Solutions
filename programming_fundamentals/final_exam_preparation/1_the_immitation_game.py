msg = input()
while True:
	command = input()
	if command == "Decode":
		print(f"The decrypted message is: {msg}")
		break
	action, *token = command.split("|")
	if action == "Move":
		count = int(token[0])
		msg = msg[count:] + msg[:count]
	elif action == "Insert":
		index, value = int(token[0]), token[1]
		msg = msg[:index] + value + msg[index:]
	elif action == "ChangeAll":
		old, new = token
		msg = msg.replace(old, new)
