hall_capacity = int(input())
price = 5
total_people = 0
income = 0
while True:
    people_entering = input()
    if people_entering == "Movie time!":
        seats_left = hall_capacity - total_people
        print(f"There are {seats_left} seats left in the cinema.")
        break
    total_people += int(people_entering)
    if total_people > hall_capacity:
        print("The cinema is full.")
        break
    else:
        income += int(people_entering) * price
        if int(people_entering) % 3 == 0:
            income -= 5

print(f"Cinema income - {income} lv.")
