import re

string = input()
cool_threshold_pattern = r"\d"
threshold_matches = re.findall(cool_threshold_pattern, string)
threshold = 1
for x in [int(s) for s in threshold_matches]:
	threshold *= x

emoji_pattern = r"((?P<sep>::|\*\*)([A-Z][a-z]{2,})(?P=sep))"
emoji_matches = re.findall(emoji_pattern, string)
cool_emojis = []
for match in emoji_matches:
	emoji = match[0]
	text = match[2]
	coolness = sum([ord(char) for char in text])
	if coolness > threshold:
		cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
print(f'{len(emoji_matches)} emojis found in the text. The cool ones are:')
for em in cool_emojis:
	print(em)
