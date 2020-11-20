text = input()

for index, char in enumerate(text):
	if char == ":":
		emoticon = char + text[index + 1]
		print(emoticon)
