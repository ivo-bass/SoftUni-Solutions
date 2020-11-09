class Zoo:
	def __init__(self, zoo_name):
		self.zoo_name = zoo_name
		self.all_animals = {"mammal": [], "fish": [], "bird": []}
		self.count_of_animals = 0

	def add_animal(self, species, name):
		self.all_animals[species].append(name)
		self.count_of_animals += 1

	def get_info(self, species):
		category = ""
		if species == "mammal":
			category = "Mammals"
		elif species == "bird":
			category = "Birds"
		elif species == "fish":
			category = "Fishes"
		return f"{category} in {self.zoo_name}: {', '.join(self.all_animals[species])}"

	def get_total(self):
		return f"Total animals: {self.count_of_animals}"


def main():
	zoo = Zoo(input())
	number = int(input())
	for _ in range(number):
		species, name = input().split()
		zoo.add_animal(species, name)
	info = input()
	print(zoo.get_info(info))
	print(zoo.get_total())


if __name__ == '__main__':
	main()
