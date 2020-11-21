data = input()
rage_quit = ""

start = 0
number = ""
for index, char in enumerate(data):
	if char.isdigit():
		stop = index - len(number)
		number += char
		if index < len(data) - 1:
			if data[index + 1].isdigit():
				continue
		rage_quit += data[start:stop].upper() * int(number)
		start = stop + len(number)
		number = ""

print(f"Unique symbols used: {len(set(rage_quit))}")
print(rage_quit)
