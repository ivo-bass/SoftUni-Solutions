string = input()

digits = []
letters = []
other = []

for char in string:
	if char.isdigit():
		digits.append(char)
	elif char.isalpha():
		letters.append(char)
	else:
		other.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(other))
