banned_words = input().split(", ")
text = input()

for word in banned_words:
	replacer = "*" * len(word)
	text = text.replace(word, replacer)

print(text)
