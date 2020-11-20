text = input()
correct_text = list(text)
for index in range(len(text)-1, 0, -1):
	if text[index] == text[index-1]:
		correct_text.pop(index)

print("".join(correct_text))
