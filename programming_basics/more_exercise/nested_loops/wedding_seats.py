# abc_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# abc_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
#              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

first_sector = "A"
last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())

sectors_range = list(map(chr, range(ord("A"), ord(last_sector)+1)))
rows = rows_first_sector
odd_seats_range = list(map(chr, range(ord("a"), ord("a") + seats_odd_row)))
even_seats_range = list(map(chr, range(ord("a"), ord("a") + seats_odd_row + 2)))
total_seats = 0

for sector in sectors_range:
    rows += 1
    for row in range(1, rows):
        if row % 2 != 0:
            for seat in odd_seats_range:
                total_seats += 1
                print(f"{sector}{row}{seat}")
        else:
            for seat in even_seats_range:
                total_seats += 1
                print(f"{sector}{row}{seat}")
print(total_seats)