def take_odd(text):
	new_text = ""
	for index in range(1, len(text), 2):
		new_text += text[index]
	print(new_text)
	return new_text


def cut(text, index, length):
	new_text = text[:index] + text[index + length:]
	print(new_text)
	return new_text


def substitute(text, substring, substitution):
	if substring in text:
		text = text.replace(substring, substitution)
		print(text)
	else:
		print("Nothing to replace!")
	return text


def main():
	password = input()

	while True:
		command = input()
		if command == "Done":
			break
		if command == "TakeOdd":
			password = take_odd(password)
		else:
			action, token1, token2 = command.split()
			if action == "Cut":
				index, length = int(token1), int(token2)
				password = cut(password, index, length)
			elif action == "Substitute":
				password = substitute(password, token1, token2)

	print(f"Your password is: {password}")


main()
