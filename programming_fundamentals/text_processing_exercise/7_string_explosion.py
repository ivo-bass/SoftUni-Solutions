text_list = list(input())

strength = 0
index = 0

for index in range(len(text_list)):
	if text_list[index] == ">" and index < len(text_list) - 1:
		strength += int(text_list[index + 1])
		while strength > 0 and index < len(text_list) - 1:
			if not text_list[index + 1] == ">":
				index += 1
				text_list[index] = "fuck"
				strength -= 1
			else:
				break

text_list = list(filter(lambda x: x != "fuck", text_list))
print("".join(text_list))
