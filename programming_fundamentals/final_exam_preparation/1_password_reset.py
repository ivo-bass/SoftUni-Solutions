def take_odd(text):
	new_text = ""
	for index, char in enumerate(text):
		if not index % 2 == 0:
			new_text += char
	print(new_text)
	return new_text


def cut(text, index, length):
	substring = text[index:index + length]
	new_text = text.replace(substring, "", 1)
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
