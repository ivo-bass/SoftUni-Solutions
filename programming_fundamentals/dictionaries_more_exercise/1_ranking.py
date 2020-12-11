def get_contests():
	contests = {}
	while True:
		data = input()
		if data == "end of contests":
			break
		contest, password = data.split(":")
		contests[contest] = password
	return contests


def get_users_data(contests):
	users = {}
	while True:
		data = input()
		if data == "end of submissions":
			break
		contest, password, username, points = data.split("=>")
		points = int(points)
		if contest not in contests or not password == contests[contest]:
			continue
		if username in users:
			if contest in users[username] and points < users[username][contest]:
				points = users[username][contest]
			users[username][contest] = points
		else:
			users[username] = {contest: points}
	return users


def calc_total_points(users):
	users_total_points = {}
	for key, value in users.items():
		total_points = sum([score for score in value.values()])
		users_total_points[key] = total_points
	return users_total_points


def print_best_candidate(users_total_points):
	best_candidate = max(users_total_points, key=lambda x: users_total_points[x])
	best_score = users_total_points[best_candidate]
	print(f"Best candidate is {best_candidate} with total {best_score} points.")


def print_all_students(users):
	print("Ranking:")
	users = dict(sorted(users.items(), key=lambda x: x[0]))
	for username, values in users.items():
		print(username)
		values = dict(sorted(values.items(), key=lambda x: -x[1]))
		for contest, points in values.items():
			print(f"#  {contest} -> {points}")


def main():
	contests = get_contests()
	users = get_users_data(contests)
	users_total_points = calc_total_points(users)
	print_best_candidate(users_total_points)
	print_all_students(users)


main()
