from re import compile

sentence = input()
regex = r"(^|(?<=\s))([a-zA-Z0-9]+([\._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([\-][a-zA-Z]+)*(\.[a-zA-Z]+)+)($|(?=\s)|\b)"
pattern = compile(regex)
emails = pattern.findall(sentence)
for email in emails:
	print(email[1])
