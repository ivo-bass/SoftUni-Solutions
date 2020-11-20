line = input().split(", ")
valid_usernames = []


def check_validity(text):
	valid_length = True if 3 <= len(text) <= 16 else False
	valid_chars = True if text.isalnum() or "-" in text or "_" in text else False
	if not valid_length or not valid_chars:
		return False
	return True


for username in line:
	if check_validity(username):
		valid_usernames.append(username)

for username in valid_usernames:
	print(username)
