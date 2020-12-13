from re import match

successful = 0
n = int(input())
for _ in range(n):
	matches = match(r"^(U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[\d]+)P@\$)$", input())
	if matches:
		successful += 1
		print("Registration was successful")
		print(f"Username: {matches[2]}, Password: {matches[3]}")
	else:
		print("Invalid username or password")

print(f"Successful registrations: {successful}")
