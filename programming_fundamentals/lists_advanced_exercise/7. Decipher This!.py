"""You are given a secret message you need to decipher."""


def decode_first_letter(string):
	"""Takes a string with a code for the first character,
	decodes the first character and returns the decoded string"""
	code = ""
	end_of_str = ""
	# Iterate over each char of the string
	# We need the index for the list slicing
	for i in range(len(string)):
		# Check if the char is a number
		if string[i].isnumeric():
			code += string[i]
		else:
			# When we reach non-integer we need to break
			# and slice the rest of the string
			end_of_str = string[i:]
			break
	# Decode the first char in ascii
	first_letter = chr(int(code))
	# Concatenate first char with the rest of the string
	return first_letter + end_of_str


def switch_second_and_last(string):
	"""Takes a string and returns the string with switched places
	of the last and the second characters"""
	# String is immutable so we turn it to a list
	li_str = [s for s in string]
	# Switch places
	li_str[1], li_str[-1] = li_str[-1], li_str[1]
	# We need to return string
	return "".join(li_str)


def main():
	"""Take an input and return the deciphered version"""
	text = input()
	# Split the text into a list
	text_list = text.split()
	deciphered_list = []
	# Iterate the item in the list, decode the item
	# and append the results in a list
	for word in text_list:
		word = decode_first_letter(word)
		word = switch_second_and_last(word)
		deciphered_list.append(word)
	# Turn the result list into a string
	deciphered = " ".join(deciphered_list)
	print(deciphered)


if __name__ == '__main__':
	main()
