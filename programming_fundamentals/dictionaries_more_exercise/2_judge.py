def update_users(users, user, points):
	if user not in users:
		users[user] = points
	else:
		users[user] += points
	return users


def update_contests(contests, users, user, contest, points):
	if contest not in contests:
		contests[contest] = {user: points}
	else:
		if user in contests[contest]:
			users[user] -= contests[contest][user]
			if contests[contest][user] > points:
				points = contests[contest][user]
		contests[contest][user] = points
	return contests, points


def print_contests(contests):
	for contest, results in contests.items():
		print(f"{contest}: {len(results)} participants")
		position = 1
		results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
		for user, points in results.items():
			print(f"{position}. {user} <::> {points}")
			position += 1


def print_users(users):
	users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
	position = 1
	print("Individual standings:")
	for user, points in users.items():
		print(f"{position}. {user} -> {points}")
		position += 1


def main():
	contests = {}
	users = {}

	while True:
		data = input()
		if data == "no more time":
			break
		user, contest, points = data.split(" -> ")
		points = int(points)
		contests, points = update_contests(contests, users, user, contest, points)
		users = update_users(users, user, points)

	print_contests(contests)
	print_users(users)


main()
