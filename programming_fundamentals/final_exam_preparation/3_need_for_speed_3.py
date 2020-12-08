def drive(cars, car, distance, fuel):
	if cars[car]["fuel"] < fuel:
		print("Not enough fuel to make that ride")
	else:
		cars[car]["fuel"] -= fuel
		cars[car]["mileage"] += distance
		print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
		if cars[car]["mileage"] >= 100_000:
			del cars[car]
			print(f"Time to sell the {car}!")
	return cars


def refuel(cars, car, fuel):
	if fuel + cars[car]["fuel"] > 75:
		fuel = 75 - cars[car]["fuel"]
	cars[car]["fuel"] += fuel
	print(f"{car} refueled with {fuel} liters")
	return cars


def revert(cars, car, kilometers):
	cars[car]["mileage"] -= kilometers
	if cars[car]["mileage"] < 10_000:
		cars[car]["mileage"] = 10_000
	else:
		print(f"{car} mileage decreased by {kilometers} kilometers")
	return cars


def get_cars():
	cars = {}
	n = int(input())
	for _ in range(n):
		car, mileage, fuel = input().split("|")
		cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
	return cars


def print_cars(cars):
	cars = dict(sorted(cars.items(), key=lambda x: (-x[1]["mileage"], x[0])))
	for car, values in cars.items():
		print(f"{car} -> Mileage: {values['mileage']} kms, Fuel in the tank: {values['fuel']} lt.")


def main():
	cars = get_cars()
	while True:
		command = input()
		if command == "Stop":
			break
		action, *values = command.split(" : ")
		if action == "Drive":
			car, distance, fuel = values[0], int(values[1]), int(values[2])
			cars = drive(cars, car, distance, fuel)
		elif action == "Refuel":
			car, fuel = values[0], int(values[1])
			cars = refuel(cars, car, fuel)
		elif action == "Revert":
			car, kilometers = values[0], int(values[1])
			cars = revert(cars, car, kilometers)
	print_cars(cars)


main()
