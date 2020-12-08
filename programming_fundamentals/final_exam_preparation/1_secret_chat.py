def insert_space(text, index):
	text = text[:index] + " " + text[index:]
	print(text)
	return text


def reverse_string(text, substring):
	if substring not in text:
		print("error")
	else:
		text = text.replace(substring, "", 1)
		substring = substring[::-1]
		text = text + substring
		print(text)
	return text


def change_all(text, substring, replacement):
	text = text.replace(substring, replacement)
	print(text)
	return text


def main():
	message = input()
	while True:
		data = input()
		if data == "Reveal":
			print(f"You have a new text message: {message}")
			break
		command = data.split(":|:")
		action = command[0]
		if action == "InsertSpace":
			index = int(command[1])
			message = insert_space(message, index)
		elif action == "Reverse":
			substring = command[1]
			message = reverse_string(message, substring)
		elif action == "ChangeAll":
			substring, replacement = command[1], command[2]
			message = change_all(message, substring, replacement)


main()
