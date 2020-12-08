from re import findall

pattern = r"([@|#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
data = input()
matches = findall(pattern, data)
mirror_words = []

for match in matches:
	if match[1] == match[2][::-1]:
		mirror_words.append(match[1] + " <=> " + match[2])

if not matches:
	print("No word pairs found!")
else:
	print(f"{len(matches)} word pairs found!")
if not mirror_words:
	print("No mirror words!")
else:
	print("The mirror words are:")
	print(", ".join(mirror_words))
