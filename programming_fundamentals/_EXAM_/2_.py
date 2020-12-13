from re import match

successful = 0
n = int(input())
for _ in range(n):
	valid = match(r"^(U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[\d]+)P@\$)$", input())
	if valid:
		successful += 1
		print("Registration was successful")
		print(f"Username: {valid[2]}, Password: {valid[3]}")
	else:
		print("Invalid username or password")

print(f"Successful registrations: {successful}")
