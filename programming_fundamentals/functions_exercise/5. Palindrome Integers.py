def check_if_polindrome(num_str):
	reversed_num_str = num_str[::-1]
	if num_str == reversed_num_str:
		return True
	else:
		return False


def main():
	list_of_string_nums = list(input().split(", "))
	for string_num in list_of_string_nums:
		print(check_if_polindrome(string_num))


if __name__ == '__main__':
	main()
