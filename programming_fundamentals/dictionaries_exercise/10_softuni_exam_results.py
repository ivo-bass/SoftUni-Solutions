class Exam:
	def __init__(self):
		self.max_results = {}
		self.submissions = {}

	def ban(self, name):
		if name in self.max_results:
			del self.max_results[name]

	def add_student(self, name):
		if name not in self.max_results:
			self.max_results[name] = 0

	def add_language(self, lang):
		if lang not in self.submissions:
			self.submissions[lang] = 0

	def add_result(self, name, lang, points):
		self.submissions[lang] += 1
		if points > self.max_results[name]:
			self.max_results[name] = points

	def sort_results(self):
		self.max_results = dict(sorted(self.max_results.items(), key=lambda x: x[0]))
		self.max_results = dict(sorted(self.max_results.items(), key=lambda x: x[1], reverse=True))

	def sort_submissions(self):
		self.submissions = dict(sorted(self.submissions.items(), key=lambda x: x[0]))
		self.submissions = dict(sorted(self.submissions.items(), key=lambda x: x[1], reverse=True))

	def get_statistics(self):
		self.sort_results()
		print("Results:")
		for name, points in self.max_results.items():
			print(f"{name} | {points}")

		self.sort_submissions()
		print("Submissions:")
		for lang, count in self.submissions.items():
			print(f"{lang} - {count}")


def main():
	exam = Exam()
	data = input()
	while not data == "exam finished":
		command = data.split("-")
		name = command[0]
		if command[1] == "banned":
			exam.ban(name)
		else:
			language, points = command[1], int(command[2])
			exam.add_student(name)
			exam.add_language(language)
			exam.add_result(name, language, points)
		data = input()
	exam.get_statistics()


if __name__ == '__main__':
	main()
