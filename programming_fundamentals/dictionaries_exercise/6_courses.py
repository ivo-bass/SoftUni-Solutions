class DataBase:
	def __init__(self):
		self.courses = {}

	def add_course(self, course, student):
		self.courses[course] = [student]

	def add_student(self, course, student):
		self.courses[course].append(student)

	def sort_courses(self):
		self.courses = {k: v for k, v in sorted(self.courses.items(), key=lambda item: len(item[1]), reverse=True)}

	def sort_students(self, students):
		students = [s for s in sorted(students)]
		return students

	def get_info(self):
		self.sort_courses()
		for course, students in self.courses.items():
			print(f"{course}: {len(students)}")

			students = self.sort_students(students)
			for student in students:
				print(f"-- {student}")


def main():
	db = DataBase()
	info = input()
	while not info == "end":
		course, student = info.split(" : ")
		if course not in db.courses.keys():
			db.add_course(course, student)
		else:
			db.add_student(course, student)
		info = input()
	db.get_info()


if __name__ == '__main__':
	main()
