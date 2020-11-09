tickets_total = 0
student = 0
standard = 0
kid = 0
while True:
    movie_name = input()
    tickets_per_movie = 0
    if movie_name == 'Finish':
        print(f"Total tickets: {tickets_total}")
        print(f"{(student / tickets_total):.2%} student tickets.")
        print(f"{(standard / tickets_total):.2%} standard tickets.")
        print(f"{(kid / tickets_total):.2%} kids tickets.")
        break
    free_seats = int(input())
    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        else:
            tickets_total += 1
            tickets_per_movie += 1
            if ticket_type == 'student':
                student += 1
            elif ticket_type == 'standard':
                standard += 1
            elif ticket_type == 'kid':
                kid += 1
    percentage_full = tickets_per_movie / free_seats
    print(f"{movie_name} - {percentage_full:.2%} full.")
