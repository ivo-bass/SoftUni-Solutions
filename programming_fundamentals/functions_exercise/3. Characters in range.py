def character_range(ch1, ch2):
	result = []
	for code in range(ord(ch1) + 1, ord(ch2)):
		result.append(chr(code))
	return result


def main():
	char_1 = input()
	char_2 = input()
	print(*character_range(char_1, char_2))


if __name__ == '__main__':
	main()
