from datetime import datetime, timedelta

birth_date = input()

struct_birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
add1000 = struct_birth_date + timedelta(1000)
future_date = datetime.strftime(add1000, "%d-%m-%Y")

print(future_date)
