PERFECT_NUMS = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]

number = int(input())

if number in PERFECT_NUMS:
	print("We have a perfect number!")
else:
	print("It's not so perfect.")
