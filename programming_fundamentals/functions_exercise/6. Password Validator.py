def check_length(text):
	if 6 <= len(text) <= 10:
		return True


def check_chars(text):
	for char in text:
		if not char.isalnum():
			return False
	return True


def check_for_digits(text):
	sum_of_digits = 0
	for char in text:
		if char.isnumeric():
			sum_of_digits += 1
	if sum_of_digits >= 2:
		return True


def password_validator(password):
	if not check_length(password):
		print("Password must be between 6 and 10 characters")
	if not check_chars(password):
		print("Password must consist only of letters and digits")
	if not check_for_digits(password):
		print("Password must have at least 2 digits")
	if check_length(password) and check_chars(password) and check_for_digits(password):
		print("Password is valid")


pas = input()
password_validator(pas)
