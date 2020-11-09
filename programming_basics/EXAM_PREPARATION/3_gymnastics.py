country = input()
discipline = input()

results = {
    "Russia": {"ribbon": 18.500, "hoop": 19.100, "rope": 18.600},
    "Bulgaria": {"ribbon": 19.000, "hoop": 19.300, "rope": 18.900},
    "Italy": {"ribbon": 18.700, "hoop": 18.800, "rope": 18.850}
}

result = results[country][discipline]
needed_points = 20 - result
percentage = needed_points / 20

print(f"The team of {country} get {result:.3f} on {discipline}.")
print(f"{percentage:.2%}")
