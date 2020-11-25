from re import compile

pattern = compile(r"(w{3}.[A-Za-z0-9-]+(\.[a-z]+)+)")

data = input()
while data:
	match = pattern.findall(data)
	if match:
		print(match[0][0])
	data = input()
