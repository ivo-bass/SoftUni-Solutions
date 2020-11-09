count_tickets = int(input())
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
place_numbers = []

for _ in range(count_tickets):
    place_number = ""
    ticket_number = input()
    ticket_length = len(ticket_number)

    if ticket_length == 4:
        if ticket_number[0] in alphabet_upper:
            place_number = f"{ticket_number[0]}{ticket_number[1]}{ticket_number[2]}"
        else:
            place_number = f"{ticket_number[3]}{ticket_number[1]}{ticket_number[2]}"
    elif ticket_length in (5, 6):
        ascii_value = ord(ticket_number[1])
        # автоматично аски се превръща в стринг
        place_number = f"{ticket_number[0]}{ascii_value}"

    place_numbers.append(place_number)

for place_number in place_numbers:
    print(f"Seat decoded: {place_number}")
