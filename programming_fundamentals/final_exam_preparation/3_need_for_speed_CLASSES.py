"""
3
Audi A6|38000|62
Mercedes CLS|11000|35
Volkswagen Passat CC|45678|5
Drive : Audi A6 : 543 : 47
Drive : Mercedes CLS : 94 : 11
Drive : Volkswagen Passat CC : 69 : 8
Refuel : Audi A6 : 50
Revert : Mercedes CLS : 500
Revert : Audi A6 : 30000
Stop
"""


class Car:
	def __init__(self, model, mileage, fuel):
		self.model = model
		self.mileage = mileage
		self.fuel = fuel

	def drive(self, distance, fuel):
		if self.fuel < fuel:
			print("Not enough fuel to make that ride")
		else:
			self.fuel -= fuel
			self.mileage += distance
			print(f"{self.model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
			if self.mileage >= 100_000:
				print(f"Time to sell the {self.model}!")
				race.cars.remove(self.model)

	def refuel(self, fuel):
		if fuel + self.fuel > 75:
			fuel = 75 - self.fuel
		self.fuel += fuel
		print(f"{self.model} refueled with {fuel} liters")

	def revert(self, kilometers):
		self.mileage -= kilometers
		if self.mileage < 10_000:
			self.mileage = 10_000
		else:
			print(f"{self.model} mileage decreased by {kilometers} kilometers")


class Race:
	def __init__(self):
		self.cars = {}

	def get_cars(self):
		n = int(input())
		for _ in range(n):
			model, mileage, fuel = input().split("|")
			self.cars[model] = Car(model, int(mileage), int(fuel))

	def print_cars(self):
		self.cars = dict(sorted(self.cars.items(), key=lambda x: (-x[1].mileage, x[0])))
		for obj in self.cars.values():
			print(f"{obj.model} -> Mileage: {obj.mileage} kms, Fuel in the tank: {obj.fuel} lt.")


def main():
	race = Race()
	race.get_cars()
	while True:
		command = input()
		if command == "Stop":
			race.print_cars()
			break
		action, *values = command.split(" : ")
		if action == "Drive":
			model, distance, fuel = values[0], int(values[1]), int(values[2])
			race.cars[model].drive(distance, fuel)
		###
		elif action == "Refuel":
			model, fuel = values[0], int(values[1])
			race.cars[model].refuel(fuel)
		elif action == "Revert":
			model, kilometers = values[0], int(values[1])
			race.cars[model].revert(kilometers)


main()
