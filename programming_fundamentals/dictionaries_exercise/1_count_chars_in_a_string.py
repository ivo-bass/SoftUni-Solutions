text = input()

occurrences = {}

for char in text:
	if not char == " ":
		if char not in occurrences.keys():
			occurrences[char] = 1
		else:
			occurrences[char] += 1

for item in occurrences.items():
	key, value = item
	print(f"{key} -> {value}")