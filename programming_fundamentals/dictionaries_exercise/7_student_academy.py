class DataBase:
	def __init__(self):
		self.all_students_grades = {}
		self.high_grade = {}

	def add_student(self, name):
		self.all_students_grades[name] = []

	def add_grade(self, name, grade):
		self.all_students_grades[name].append(grade)

	def get_average_grade(self):
		for name, grades in self.all_students_grades.items():
			average = sum(grades) / len(grades)
			self.high_grade[name] = average

	def filter_students(self):
		self.high_grade = dict(filter(lambda item: item[1] >= 4.5, self.high_grade.items()))

	def sort_students(self):
		self.high_grade = dict(sorted(self.high_grade.items(), key=lambda item: item[1], reverse=True))

	def print_students(self):
		for name, grade in self.high_grade.items():
			print(f"{name} -> {grade:.2f}")


def main():
	db = DataBase()
	rows = int(input())
	name = ""
	for row in range(1, rows * 2 + 1):
		if not row % 2 == 0:
			name = input()
			if name not in db.all_students_grades.keys():
				db.add_student(name)
		else:
			grade = float(input())
			db.add_grade(name, grade)
	db.get_average_grade()
	db.filter_students()
	db.sort_students()
	db.print_students()


if __name__ == '__main__':
	main()
