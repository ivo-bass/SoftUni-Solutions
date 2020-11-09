flights = []

while True:
    number = input()
    if number == "End":
        break
    price = float(input()) * 1.96
    minutes = int(input())
    flights.append((number, price, minutes))

min_minutes = flights[0][2]
min_minutes_flight = flights[0]
for flight in flights:
    if flight[2] < min_minutes:
        min_minutes = flight[2]
        min_minutes_flight = flight

number = min_minutes_flight[0]
price = min_minutes_flight[1]
hours = min_minutes // 60
mins = min_minutes % 60

output_string = "Ticket found for flight {} costs {:.2f} leva with {}h {}m stay"
print(output_string.format(number, price, hours, mins))
