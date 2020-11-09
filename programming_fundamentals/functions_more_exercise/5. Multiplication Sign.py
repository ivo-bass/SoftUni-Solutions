def count_negative_numbers(li):
	filter_negative = list(filter(lambda x: x < 0, li))
	count = len(filter_negative)
	return count


def multiplication_sign(n1, n2, n3):
	nums = [n1, n2, n3]
	if 0 in nums:
		return "zero"
	elif count_negative_numbers(nums) % 2 == 0:
		return "positive"
	else:
		return "negative"


def main():
	num1 = float(input())
	num2 = float(input())
	num3 = float(input())
	print(multiplication_sign(num1, num2, num3))


if __name__ == '__main__':
	main()
