text = input()

while not text == 'end':
	print(f"{text} = {text[::-1]}")
	text = input()
