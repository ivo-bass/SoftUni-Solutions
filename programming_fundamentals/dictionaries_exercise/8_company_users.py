class DataBase:
	def __init__(self):
		self.companies = {}

	def add_company(self, company):
		if company not in self.companies.keys():
			self.companies[company] = []

	def add_id(self, company, i_d):
		if i_d not in self.companies[company]:
			self.companies[company].append(i_d)

	def sort_companies(self):
		"""Returns the companies ordered ascending by name"""
		return dict(sorted(self.companies.items(), key=lambda item: item[0]))

	def print_companies(self):
		self.companies = self.sort_companies()
		for company, i_ds in self.companies.items():
			print(f"{company}")
			for i_d in i_ds:
				print(f"-- {i_d}")


def main():
	# Generate an instance of the DataBase class
	db = DataBase()
	# Receive data until "End" command
	data = input()
	while not data == "End":
		company, i_d = data.split(" -> ")
		db.add_company(company)
		db.add_id(company, i_d)
		data = input()
	db.print_companies()


if __name__ == '__main__':
	main()
