class DataBase:
	"""Keeps information about companies and their employees"""
	def __init__(self):
		self.companies = {}

	def add_company(self, company):
		"""Adds company in database if not existing"""
		if company not in self.companies.keys():
			self.companies[company] = []

	def add_id(self, company, i_d):
		"""Adds employee to the given company.
		A company cannot have two employees with the same id"""
		if i_d not in self.companies[company]:
			self.companies[company].append(i_d)

	def sort_companies(self):
		"""Orders the companies by the name in ascending order"""
		self.companies = dict(sorted(self.companies.items(), key=lambda item: item[0]))

	def print_companies(self):
		"""Prints the company name and each employee's id."""
		for company, i_ds in self.companies.items():
			print(f"{company}")
			for i_d in i_ds:
				print(f"-- {i_d}")


def main():
	"""8. Company Users / Dictionaries Exercise
	Write a program that keeps information about companies and their employees."""
	# Generate instance of database
	db = DataBase()

	# Receive data until "End" command
	data = input()
	while not data == "End":
		company, i_d = data.split(" -> ")
		db.add_company(company)
		db.add_id(company, i_d)
		data = input()

	db.sort_companies()
	db.print_companies()


if __name__ == '__main__':
	main()
