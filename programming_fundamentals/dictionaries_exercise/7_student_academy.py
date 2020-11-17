class Student:
	def __init__(self, name, grade):
		self.name = name
		self.grades = [grade]
		self.average_grade = grade
		self.is_top_student = True if self.average_grade >= 4.5 else False

	def calc_avrg_grade(self):
		self.average_grade = sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0
		self.is_top_student = True if self.average_grade >= 4.5 else False


class DataBase:
	def __init__(self):
		self.students = []
		self.top_students = []

	def add_info(self, name, grade):
		if self.students:
			for student in self.students:
				if student.name == name:
					student.grades.append(grade)
					student.calc_avrg_grade()
					return
		self.students.append(Student(name, grade))

	def sort_students(self):
		self.top_students = [cl for cl in self.students if cl.is_top_student]
		self.top_students = sorted(self.top_students, key=lambda x: -x.average_grade)

	def print_students(self):
		self.sort_students()
		for student in self.top_students:
			print(f"{student.name} -> {student.average_grade:.2f}")


db = DataBase()
rows = int(input())
for row in range(1, rows * 2 + 1):
	if not row % 2 == 0:
		n = input()
		gr = float(input())
		db.add_info(name=n, grade=gr)
db.print_students()
