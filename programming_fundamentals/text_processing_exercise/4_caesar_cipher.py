text = list(input())

encrypted = []

for char in text:
	encrypted.append(chr(ord(char) + 3))

print("".join(encrypted))
