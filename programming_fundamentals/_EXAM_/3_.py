def add_user(users, username):
	if username in users:
		print(f"{username} is already registered")
	else:
		users[username] = []
	return users


def send_email(users, username, email):
	users[username].append(email)
	return users


def delete_user(users, username):
	if username not in users:
		print(f"{username} not found!")
	else:
		del users[username]
	return users


def print_info(users):
	users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
	print(f"Users count: {len(users)}")
	for user, emails in users.items():
		print(f"{user}")
		for email in emails:
			print(f" - {email}")


def main():
	users = {}
	while True:
		command = input()
		if command == "Statistics":
			break
		action, *token = command.split("->")
		if action == "Add":
			username = token[0]
			users = add_user(users, username)
		elif action == "Send":
			username, email = token
			users = send_email(users, username, email)
		elif action == "Delete":
			username = token[0]
			users = delete_user(users, username)
	print_info(users)


main()
