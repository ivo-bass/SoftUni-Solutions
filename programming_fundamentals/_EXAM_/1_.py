text = input()

while True:
	command = input()
	if command == "End":
		break
	command = command.split()
	action = command[0]
	if action == "Translate":
		char, replacement = command[1], command[2]
		text = text.replace(char, replacement)
		print(text)
	elif action == "Includes":
		substring = command[1]
		if substring in text:
			print("True")
		else:
			print("False")
	elif action == "Start":
		substring = command[1]
		if text[:len(substring)] == substring:
			print("True")
		else:
			print("False")
	elif action == "Lowercase":
		text = text.lower()
		print(text)
	elif action == "FindIndex":
		char = command[1]
		last_i = 0
		for i, c in enumerate(text):
			if c == char:
				last_i = i
		print(last_i)
	elif action == "Remove":
		start_i, count = int(command[1]), int(command[2])
		text = text[:start_i] + text[start_i + count:]
		print(text)
