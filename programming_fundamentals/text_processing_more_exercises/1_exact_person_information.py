class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


lines = [input() for line in range(int(input()))]
persons = []
for line in lines:
	name = line[line.index("@")+1:line.index("|")]
	age = line[line.index("#")+1:line.index("*")]
	persons.append(Person(name, age))

for person in persons:
	print(f"{person.name} is {person.age} years old.")
