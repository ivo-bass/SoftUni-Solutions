def sum_odd_and_even_digits(num_str):
	odd_sum = 0
	even_sum = 0
	num_list = [int(s) for s in num_str]
	for num in num_list:
		if num % 2 == 0:
			even_sum += num
		else:
			odd_sum += num
	return odd_sum, even_sum


def main():
	get_num_as_string = input()
	odds, evens = sum_odd_and_even_digits(get_num_as_string)
	print(f"Odd sum = {odds}, Even sum = {evens}")


if __name__ == '__main__':
	main()
